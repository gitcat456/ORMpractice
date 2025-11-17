from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User  # Import your custom User model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User  # Which model this form saves to
        fields = ('username', 'email', 'first_name', 'phone_number', 'password1', 'password2') #Which fields should be shown
      

    def save(self, commit=True):  #overide the default form save method
        user = super().save(commit=False) # build the user, don't save
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
    
        # All new users are customers by default
        user.role = 'customer'
        
        if commit:
            user.save()   # finally save to DB
        return user  # return the final user object
    
    
User = get_user_model  # get the active user model without hardcoding ie from accounts.User

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
        }