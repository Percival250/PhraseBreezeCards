from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditProfile(forms.ModelForm):

    username = forms.CharField(
        label='Username',
        max_length=150,
    )
    email = forms.EmailField(
        label='Email address'
    )

    class Meta:
        model = User
        fields = ['username', 'email']
