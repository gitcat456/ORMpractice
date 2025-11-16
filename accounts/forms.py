from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User  # Import your custom User model

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