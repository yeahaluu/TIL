from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    # little customize
    class Meta:
        model = User
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):
    address = forms.CharField(min_length=3, max_length=200)
    first_name = forms.CharField(min_length=1, max_length=100)
    last_name = forms.CharField(min_length=1, max_length=100)
    email = forms.EmailField(min_length=1)
    password = None

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'address', 'email', )