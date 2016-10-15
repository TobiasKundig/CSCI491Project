#takes a request and sends back an httpresponse
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views import View

#always pass in a request and return a response
def index(request):


    return render(request,'portfolio/index.html')



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

