from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, validate_email

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Username",
    }), validators=[
        MinLengthValidator(5, "Минимум 5 символов")
    ])
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
    }), validators=[
        validate_email
    ])
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class LoginForm(AuthenticationForm):
 
    username = forms.CharField(widget=forms.TextInput(attrs={
        'Placeholder': 'Username', 'name': 'username',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'Placeholder': 'Password', 'name': 'password',
    }))
    
    class Meta:
        model = User
        fields = ['username', 'password1']
        
        
class TaskCreateForm(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Додайте завдання', 'id': 'new-task',
    }))
    
    class Meta:
        model = Task
        fields = ('title',)