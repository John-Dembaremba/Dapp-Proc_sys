from django.shortcuts import render
from .models import Product, Profile
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, BidForm
from smartContract.ETHApi import API
from .doc_validity import zimra_validity, praz_validity, prediction
from datetime import datetime, timezone
import json
import heapq
from web3.exceptions import ContractLogicError as revert_error
# Create your views here.

class Welcome_view(ListView):
    model = Product
    context_object_name = 'welcome'
    template_name = 'welcome.html'

def home(request):
    products = Product.objects.all()
    
    return render(request, 'home.html', {"products": products})

def reversed_iteration(list_):
    """
    The method reversed the last element to be the 1st
    """
    reversed_list = []
    for item in reversed(list_):
        reversed_list.append(item)
    return reversed_list

def grp_latest(list_name):
    #Method that groups events from the largest blockNumber to the smallest

    updated_list = heapq.nlargest(len(list_name), list_name, key=lambda x: x['blockNumber'])
    return updated_list

def jobs_view(request, pk):
    jobs = get_object_or_404(Product, pk=pk)
    tenders_list = []
    api = API.WebAPI()
    
    tenders = api.get_events_jobs()
    bidders = api.get_events_bidders()
    winners = api.get_winner_events_bidders()

    for event in tenders:
        my_event = event
        tenders_list.append(my_event)

    updated_list = reversed_iteration(tenders_list)
    all_events = tenders_list
    
    for bider in bidders:
        all_events.append(bider)
        for winner in winners:
            all_events.append(winner)

    from_largest = grp_latest(all_events)
    
    return render(request, 'jobs.html', {"jobs": jobs, "events": updated_list, "transactions": from_largest})

def to_list(myString):
    #converts string to list by removing '()' using replace() and split()==> list
    return myString.replace('(', '').replace(')', '').split(", ")

def to_dict(myList, sender_acc):
    """
    1. Checks if the list from to_list has 2 or just 1 element
    2. If 2 elements==> returns dict with awarded bidder info from block_num, events and job_id ==> post awarded bidder to blockchain
    3. 1 element==> returns events and job_id
    """
    _list = to_list(myList)
    sender = sender_acc

    if len(_list) == 2:
        block_num = _list[0]
        job_id = _list[1]
        handle_error = False    
        mylist = []
        bidder_info = []
        api = API.WebAPI()
        
        jobs_events = api.get_events_jobs()
        bidders_events = api.get_events_bidders()
        
        for job in jobs_events:
            for bidder in bidders_events:
                if job['args']['job'] == bidder['args']['job_id']:
                    mylist.append(bidder)
        try:
            for bidder in bidders_events:
                if bidder['blockNumber'] == int(block_num): 
                    bidder_info.append(bidder)
                    
                    api.award_bidder(user=sender,
                        job_id=bidder['args']['job_id'],
                        name=bidder['args']['name'],
                        unit_price=bidder['args']['price_unity'],
                        total_price=bidder['args']['total_price'],
                        zimra=bidder['args']['zimraITF263'],
                        praz=bidder['args']['praz'],
                        doc_validity=bidder['args']['validity']
                        )
        except revert_error as error:
            handle_error = True
        
        from_latest = grp_latest(mylist)
        context = {
                    "block": bidder_info, 
                    "events": from_latest,
                    "job_num": int(job_id),
                    "is_awarded": handle_error
                    }
        
       
    else:
        job_id = _list[0]

        mylist = []
        api = API.WebAPI()
        
        jobs_events = api.get_events_jobs()
        bidders_events = api.get_events_bidders()
        
        for job in jobs_events:
            for bider in bidders_events:
                if job['args']['job'] == bider['args']['job_id']:
                    mylist.append(bider)
        context = {
                    "events": grp_latest(mylist),
                    "job_num": int(job_id)
                }

    return context


def bidders_view(request, pk):
    jobs = get_object_or_404(Product, pk=pk)
    job_number = request.POST.get('job_num', None)
    eth_acc = request.user.profile.EthereumAccount

    context = to_dict(job_number, eth_acc)
    context["jobs"] = jobs 

    api = API.WebAPI()
    event_winners_bidders = api.get_winner_events_bidders()
    awarded_bidders = []
    
    for bider in event_winners_bidders:
        try:
            if bider.args.job_id == int(to_list(job_number)[1]):
                awarded_bidders.append(bider)
            
        except:
            if bider.args.job_id == int(to_list(job_number)[0]):
                awarded_bidders.append(bider)
            

    context['winner'] = awarded_bidders
    
    return render(request, 'bidders.html', context)
 

def post_jobs_view(request, pk):
    job = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            name = str(request.user)
            product_type = str(job)
            product = form.cleaned_data['product']
            requirements = form.cleaned_data['requirements']
            delivery_period = str(form.cleaned_data['delivery_period'])
            
            user_acc = request.user.profile.EthereumAccount
            created_date = str(datetime.now(timezone.utc))
            
            api = API.WebAPI()
            
            api.post_jobs(user=user_acc, name=name, product_type=product_type, product=product, requiments=requirements, date=created_date, delivery_period=delivery_period)

            return redirect("jobs", pk=job.pk)

    else:
        form = PostForm()
    
    return render(request, 'post_job.html', {"job": job, "form":form})

def bid_view(request, pk):
    job = get_object_or_404(Product, pk=pk)    

    if request.method == "POST":
        form = BidForm(request.POST, request.FILES)

        if form.is_valid():
            unit_price = str(form.cleaned_data['unit_price'])
            total_price = str(form.cleaned_data['total_price'])
            name = str(request.user)
            job_id = int(form.cleaned_data['job_id'])
            user_acc = request.user.profile.EthereumAccount
            zimra_date = zimra_validity(request.FILES['zimra'])
            praz_date = praz_validity(request.FILES['praz'])
            doc_validity = prediction(request.FILES['zimra'], request.FILES['praz'])
            api = API.WebAPI()
           
            api.apply_jobs(user=user_acc, job_id=job_id, name=name, unit_price=unit_price, total_price=total_price, zimra=zimra_date, praz=praz_date, doc_validity=doc_validity)
            
            return redirect("jobs", pk=job.pk)

    else:
        form = BidForm()

    

    return render(request, 'bid_job.html', {"form": form, "job": job})


def block_info(block_number):
    api = API.WebAPI()
    block_info = api.get_block(block_number)
    return block_info

def user_profile(user_name):
    eth_acc = Profile.objects.values_list('EthereumAccount', flat=True).get(user__username=user_name)
    location = Profile.objects.values_list('address', flat=True).get(user__username=user_name)
    email = User.objects.values_list('email', flat=True).get(username=user_name)
    phone = Profile.objects.values_list('contacts', flat=True).get(user__username=user_name)
    details_list = [eth_acc, location, email, phone]
    return details_list

def bider_info_view(request, pk):
    job = get_object_or_404(Product, pk=pk) 
    job_id = request.POST.get("tender_id", None)
    
    bidder_list = []
    client_list = []
    api = API.WebAPI()
    bidders_events = api.get_events_bidders()
    client_events = api.get_events_jobs()
    
    for bidder in bidders_events:
        if bidder['args']['job_id'] == int(job_id):
            user = user_profile(bidder['args']['name'])
            
            bidder_info = {
                        "suppler_info": bidder,
                        "user_details": user,
                        "block_data": block_info(bidder["blockNumber"])
                         }                 
            bidder_list.append(bidder_info)

            for client in client_events:
                if client['args']['job'] == bidder['args']['job_id']:
                    client_list.append(client)
            break
    

    context = {"job": job, "list": bidder_list, "client": client_list}
    
    return render(request, 'bider_info.html', context)

    
def client_info_view(request, pk):
    job = get_object_or_404(Product, pk=pk)

    job_id = request.POST.get("job_num", None)
    
    client_list = []
    api = API.WebAPI()
    client_events = api.get_events_jobs()
    client_list = []

    for client in client_events:
        if client['args']['job'] == int(job_id):
            user = user_profile(client['args']['name'])
            
            client_info = {
                        "client_info": client,
                        "user_details": user,
                        "block_data": block_info(client["blockNumber"])
                         }                 
            client_list.append(client_info)


    context = {"job": job, "list": client_list}
    
    return render(request, 'client_info.html', context)