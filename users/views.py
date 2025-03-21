from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user automatically
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('orders:home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    
    return render(request, "users/register.html", {"form": form})

@login_required
def home(request):
    return render(request, "users/home.html")
