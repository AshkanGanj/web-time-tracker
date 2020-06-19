'''
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
'''

from django.shortcuts import render, redirect
from .models import Sites, UserProfile

from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from TimeTracker.forms import RegisterForm
from insctructions.aggregator import Aggregators

from datetime import datetime

class IndexView(LoginRequiredMixin, generic.View):
    """View for home page"""
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        q = Sites.objects.filter(user_id=request.user.id)
        sites = q.order_by('date').all()
        aggr_daily = Aggregators(request.user.id)
        today = q.filter(date=datetime.now()).all()

        context = {
            'sites': sites,
            'today':today,
            'max': aggr_daily.max(),
            'min': aggr_daily.min(),
            'avg': aggr_daily.average(),
            'sum': aggr_daily.sum()
        }
        return render(request, 'home.html', context)


class UserList(UserPassesTestMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = UserProfile
    template_name = 'admin_view.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser


class UserDetails(UserPassesTestMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Sites
    template_name = 'admin_view.html'
    context_object_name = 'details'
    queryset = Sites.objects.all()

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = UserProfile.objects.get(id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        """filter by user_id"""
        return self.queryset.filter(user_id=self.kwargs.get('pk'))


class LoginUser(generic.View):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('user_list')
            else:
                return redirect('home')
        else:
            messages.info(request, 'email or password is incorect')
            return render(request, 'login.html')

    def get(self, request):
        return render(request, 'login.html')


class Logout(generic.View):
    def get(self, request):
        logout(request)
        return redirect('login')


class ClearSites(LoginRequiredMixin, generic.View):
    def get(self, request):
        q = Sites.objects
        sites = q.filter(user_id=request.user.id).all().delete()
        return redirect('home')

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
