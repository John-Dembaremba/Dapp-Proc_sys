from django import forms

class PostForm(forms.Form):
    product = forms.CharField(max_length=25)

    requirements = forms.CharField(widget=forms.Textarea(
           attrs={'rows':8, 'placeholder':'Describe product features'}
        ),
         max_length=200)

    delivery_period = forms.IntegerField()
   


class BidForm(forms.Form):
    job_id = forms.CharField()
    zimra = forms.FileField(max_length=30)
    praz = forms.FileField(max_length=30)
    unit_price = forms.DecimalField(decimal_places=2, max_digits=65)
    total_price = forms.DecimalField(decimal_places=2, max_digits=65)
    

