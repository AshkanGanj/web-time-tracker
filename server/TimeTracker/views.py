'''
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
'''

from django.shortcuts import render, redirect
from .models import Sites, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from TimeTracker.forms import Login, RegisterForm

from insctructions.aggregator import Aggregators
from insctructions.dataFunc import DataInstruct

@login_required(login_url='login')
def index(request):
    
    q = Sites.objects
    sites = q.filter(user_id=request.user.id).order_by('time').all()
    aggrDaily = Aggregators(request.user.id)

    context = {
        'sites': sites,
        'max': aggrDaily.max(),
        'min': aggrDaily.min(),
        'avg': aggrDaily.average(),
        'sum': aggrDaily.sum()
        }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def clearSites(request):
    q = Sites.objects
    sites = q.filter(user_id=request.user.id).all().delete()
    return redirect('home')


def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'email or password is incorect')
    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('name')
                messages.success(request, 'account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'signUp.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
