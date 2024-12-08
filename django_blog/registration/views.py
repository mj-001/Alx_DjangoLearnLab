from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import ProfileForm  # We'll create this form later

# Create your views here.

@login_required
def profile_view(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'registration/profile.html')


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful!")
            return redirect('profile')  # Redirect to profile page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# User Login View (using Django's built-in view)
from django.contrib.auth.views import LoginView

# User Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('login')

# Profile Management View
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user)
    return render(request, 'profile.html', {'profile_form': profile_form})
