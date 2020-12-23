from django.shortcuts import render, redirect

from django.contrib.auth import login
from .forms import UserRegistrationForm,UserLoginForm
# Create your views here.


def frontpage(request):
    return render(request, 'index.html')


def SignUp(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)

def LogIn(request):
    if request.method == "POST":

        form = UserLoginForm(request.POST)

        if form.is_valid():
            login(request, form.user_cache)

            return redirect('frontpage')
    
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'login.html', context)



