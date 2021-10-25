from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from src.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    
    class Meta:
              model = User
              fields = ('username', 'email', 'password1', 'password2')   

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')

class UpdateFormUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'contacts')
