


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

urlpatterns = [


url(r'^admin/', include(admin.site.urls)),
url(r'^', include('portfolio.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

