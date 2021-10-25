from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from .forms import SignUpForm, UpdateForm, UpdateFormUserProfile
from django.db import transaction
from smartContract.ETHApi import API
from django.utils.text import slugify
# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()        

    return render(request, 'signup.html', {"form":form})

@transaction.atomic
def update_profile(request):
    #Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form = UpdateForm(request.POST, instance=request.user)
        profile_form = UpdateFormUserProfile(request.POST, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile = profile_form.save(commit=False)
            '''
            get user id and relate it to eth accounts
            '''
            web3 = API.WebAPI()
            account_list = web3.Accounts
            user_id = request.user.id
            profile.EthereumAccount = account_list[user_id]
            #print(account_list[user_id])
            profile.save()
            return redirect('home')
 

    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = UpdateFormUserProfile(instance=request.user.profile)

    return render(request, 'my_account.html', {"user_form":user_form, "profile_form":profile_form})

