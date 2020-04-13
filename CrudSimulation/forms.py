from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
# from .externs.subject_types import RoleDeclaredTypes
from .models import UserCredentials
from django.contrib.auth.forms import AuthenticationForm

class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = UserCredentials
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'validationUsername', 'placeholder': 'Required'}),
            'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'validationPassword', 'placeholder': 'Required'}),
        }
    username = forms.CharField(min_length=2, max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationUsername', 'placeholder': 'Required'}))
    password = forms.CharField(min_length=2, max_length=128, required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'validationPassword', 'placeholder': 'Required'}))

# class UserTaskAdditionForm(forms.ModelForm):
#     pass

# class UserTaskDeletionForm(forms.ModelForm):
#     pass

# class UserTaskUpdateForm(forms.ModelForm):
#     pass
