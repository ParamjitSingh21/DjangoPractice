from django.shortcuts import render, redirect

from django.contrib.auth import login
from .forms import UserRegistrationForm
# Create your views here.


def frontpage(request):
    return render(request, 'index.html')


def SignUp(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)
        print(form,form.is_valid())
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


def resetPasswordConfirmation(request):
    # An email has been sent with instruction to reset your password
    pass