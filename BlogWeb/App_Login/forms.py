from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserProfile

class UserSignUp(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserEditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

class AddProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)