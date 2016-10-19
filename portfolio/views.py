from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse

from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import User
from .SQLFacade import *
#always pass in a request and return a response
def index(request):
     all_users = User.objects.all()

     return render(request, 'portfolio/index.html', {'all_users': all_users})
   # return render(request,'portfolio/index.html')

def detail(request, account):
    #if not request.user.is_authenticated():
        #return render(request, 'portfolio/login.html')
    #else:


    account = get_object_or_404(Account, username=account)
    portfolio = get_object_or_404(Portfolio, portfolio=account)
    return render(request, 'portfolio/detail.html', {'this_account': account})


def login(request):


    return

def logout(request):


    return
def authenticate(request):


    return

def signup(request):

    return


class portfolio(View):
    portfolio = "myportfolio"

    def get(self, request):

        return HttpResponse(self.portfolio)

