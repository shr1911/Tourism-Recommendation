from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, Textarea
from recommendations.models import UserSurvey


#from accounts.models import Post



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




class UserSurveyForm(ModelForm):
    # home_delivery = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # smoking = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # alcohol = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
    # wifi = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
    # valetparking = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
    # rooftop = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')



    class Meta:
        model = UserSurvey
        fields = [ 'home_delivery', 'smoking','alcohol', 'wifi', 'valetparking', 'rooftop']
        
        