from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


#what will be included on the administrative site.

admin.site.register(Portfolio)
admin.site.register(Photos)
admin.site.register(Blog)
admin.site.register(Post)


