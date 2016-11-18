from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', RegisterView.as_view(), name='register'), #registration page
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'), #the logged in users own profile
    url(r'^(?P<user>[\w\-]+)/$', views.detail, name='detail'),
    url(r'^(?P<user>[\w\-]+)/images/$', ImageManagementView.as_view(), name='image_listing'), #the logged in users own profile
    url(r'^(?P<user>[\w\-]+)/edit/$', PortfolioUpdate.as_view(), name='portfolio_update'),
]