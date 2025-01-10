from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone number'}))
    address1 = forms.CharField(label="Address1",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter primary address'}))
    address2 = forms.CharField(label="Address2",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter secondary address'}))
    city = forms.CharField(label="City",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter city name'}))
    state = forms.CharField(label="State",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter state name'}))
    pincode = forms.CharField(label="Pincode",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter pin number'}))
    country = forms.CharField(label="Country",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Country name'}))
    class Meta:
        model=Profile
        fields=['phone','address1','address2','city','state','pincode','country']


