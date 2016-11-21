
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
from .forms import *

#pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView

#always pass in a request and return a response
def index(request):

     return render(request, 'portfolio/index.html')
   # return render(request,'portfolio/index.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
    
# profile and detail are different ways to access a portfolio. It depends on context.
def profile(request):
    #user object
    user = get_object_or_404(User, username=request.user)
    userPortfolio = Portfolio.get_manageable_object_or_404(request.user, user=user)

    return render(request, 'portfolio/portfolio/portfolio.html', {'portfolio': userPortfolio})

#present the details of a portfolio.
def detail(request, user):
    #get user object based on username
    thisuser = get_object_or_404(User, username=user)

    userPortfolio = get_object_or_404(Portfolio, user=thisuser)
    #passback the object. The template will ask for properties.
    return render(request, 'portfolio/portfolio/portfolio.html', {'portfolio': userPortfolio})



class RegisterView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'portfolio/register.html')

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']




        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')
        return render(request, 'portfolio/register.html')



class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return None
    def post(self, request, *args, **kwargs):
        return None


class PortfolioUpdate(View):

    #used to override the primary key as an identifier
    def get(self, request, user, *args, **kwargs):

        user = get_object_or_404(User, username=user)

        userPortfolio = Portfolio.get_manageable_object_or_404(request.user, user=user)

        form = PortfolioForm(instance = userPortfolio)


        return render(request, 'portfolio/portfolio/edit.html', {'form': form, 'this_portfolio': userPortfolio, 'this_user': user})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user)
        portfolio = get_object_or_404(Portfolio, user=user.pk)

        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)

            portfolio.save()

            return HttpResponseRedirect(reverse('profile'))

class ProjectCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProjectForm()

        return render(request, 'portfolio/project/create.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)

            project.save()
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


#gets images of a specific portfolio
class ImageManagementView(ListView):
    def get(self, request, user):
        user = get_object_or_404(User, username=user)
        userPortfolio = get_object_or_404(Portfolio, user=user.pk)
        images = ImageContent.objects.filter(portfolio=userPortfolio.id)
        return render(request, 'portfolio/images.html', {'images': images})




def listing(request):
    image_list = ImageContent.objects.all()
    paginator = Paginator(image_list, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)

    return render(request, 'portfolio/images.html', {'images': images})

def ImageContentList(View):

    def get(self, request, *args, **kwargs):

        user = get_object_or_404(User, username=request.user)
        userPortfolio = get_object_or_404(Portfolio, user=user.pk)
        images = ImageContent.objects.get(portfolio=userPortfolio.id)


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