from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import LoginView
from .views import RegisterView

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', RegisterView.as_view(), name='register'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),

    url(r'^(?P<user>[\w\-]+)/$', views.detail, name='detail'),

]