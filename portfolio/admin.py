from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Account, User, Portfolio


#what will be included on the administrative site.
admin.site.register(Account)
admin.site.register(User)
admin.site.register(Portfolio)
