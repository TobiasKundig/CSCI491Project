from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import User
from .SQLFacade import *

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


#forms
from .forms import User_Registration

#always pass in a request and return a response
def index(request):
     #check if logged in


     all_users = User.objects.all()

     return render(request, 'portfolio/index.html', {'all_users': all_users})
   # return render(request,'portfolio/index.html')

def profile(request):
    profile = get_object_or_404(User, username=request.user)



    return render(request, 'portfolio/portfolio.html', {'this_account': profile})
#present the details of a portfolio.
def detail(request, user):
    #if not request.user.is_authenticated():
        #return render(request, 'portfolio/login.html')
    #else:

    #profile object = Model, where username=user
    profile = get_object_or_404(User,username=user)

    #passback the object. The template will ask for properties.
    return render(request, 'portfolio/portfolio.html', {'this_account': profile})

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = User_Registration()
        return render(request, 'portfolio/register.html', {'form': form})

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        form = User_Registration(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect('login')
        return render(request, 'portfolio/register.html', {'form': form})
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return None
    def post(self, request, *args, **kwargs):
        return None

class LoginView(View):

    template_name = ['portfolio/login.html', 'portfolio/portfolio.html']

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated():

            return redirect('profile')
        return render(request, self.template_name[0])

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_active:
                return redirect('profile')
        else:
            messages.add_message(
                request, messages.ERROR, "Invalid username or password"
            )
            return HttpResponseRedirect(reverse('portfolio:login'))

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('portfolio:index'))

