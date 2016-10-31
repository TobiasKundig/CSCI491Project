from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile


#what will be included on the administrative site.
admin.site.register(Profile)

