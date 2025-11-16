# accounts/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class AdminRequiredMixin(UserPassesTestMixin):
    """Verify that the current user is an admin."""
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin()
    
    def handle_no_permission(self):
        return redirect('home')  # Redirect non-admins to home page

class CustomerRequiredMixin(UserPassesTestMixin):
    """Verify that the current user is a customer."""
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_customer()
    
    def handle_no_permission(self):
        return redirect('home')