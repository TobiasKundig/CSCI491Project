#takes a request and sends back an httpresponse
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
#always pass in a request and return a response
def index(request):

    return render_to_response('src/index.html')
