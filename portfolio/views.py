
from django.contrib.auth.models import User


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, FormView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import PortfolioForm
from .models import *
from django.core.files.storage import FileSystemStorage
#forms
from .forms import User_Registration


#always pass in a request and return a response
def index(request):

     return render(request, 'portfolio/index.html')
   # return render(request,'portfolio/index.html')


# profile and detail are different ways to access a portfolio. It depends on context.
def profile(request):
    #user object
    user = get_object_or_404(User, username=request.user)
    userPortfolio = get_object_or_404(Portfolio, user = user.pk )

    return render(request, 'portfolio/portfolio.html', {'this_account': userPortfolio})

#present the details of a portfolio.
def detail(request, user):
    #get user object based on username
    thisuser = get_object_or_404(User, username=user)


    userPortfolio = Portfolio.get_manageable_object_or_404(request.user, user=thisuser)



    #passback the object. The template will ask for properties.
    return render(request, 'portfolio/portfolio.html', {'portfolio': userPortfolio})



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


class PortfolioUpdate(View):

    #used to override the primary key as an identifier
    def get(self, request, *args, **kwargs):

        form = PortfolioForm()
        user = get_object_or_404(User, username=request.user)
        userPortfolio = get_object_or_404(Portfolio, user=user.pk)

        return render(request, 'portfolio/edit.html', {'form': form, 'this_portfolio': userPortfolio, 'this_user': user})

    def post(self, request, *args, **kwargs):

        name = request.POST.get('txtName')
        header = request.POST.get('txtHeader')
        style = request.POST.get('selectStyle')

        if request.FILES['inputImg']:
            img = request.FILES['inputImg']

        Portfolio.objects.update(name=name, header=header, style=style, img=img)

        return HttpResponseRedirect(reverse('profile'))

def TextContentUpdate(View):

    def get(self, request, id, *args, **kwargs):
        #check to see if the user has permission to edit this post.
        if request.user.is_authenticated():
            item = TextContent.get_manageable_object_or_404(request.user, id=id)

        #if not, give them a message.
        #else:

        content = get_object_or_404(TextContent)
    def post(self, request, *args, **kwargs):
        content = request.POST['text']

def ImageContentUpdate(View):

    def get(self, request, *args, **kwargs):
        content = get_object_or_404(ImageContent)
    def post(self, request, *args, **kwargs):
        content = request.POST['imgContent']


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

class CannotManage(Exception):
    pass
