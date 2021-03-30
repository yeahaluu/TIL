from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

user = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = user
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = ('last_name', 'first_name',)