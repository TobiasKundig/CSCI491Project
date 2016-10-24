
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^$', include('portfolio.urls'))

]
