from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def register(request):
    # If the request is POST the form will be passed in
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        # If the form is valid the user will receive a prompt and be redirected to the homepage
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created! Please Log In!")
            return redirect('login-user')
        # If the form is NOT valid a registration form will be returned
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
