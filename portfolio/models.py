from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404

class Portfolio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    header = models.CharField(max_length=150)
    style = models.CharField(max_length=30)
    img = models.ImageField(default=None,verbose_name='main', upload_to='Portfolio/%Y/%m/%d')

    def user_can_manage_me(self, thisuser):

        return thisuser == self.user or thisuser.has_perm('Portfolio.manage_object')

    @classmethod
    def get_manageable_object_or_404(cls, thisuser, *args, **kwds):
        item = get_object_or_404(cls, *args, **kwds)
        if not item.user_can_manage_me(thisuser):
            raise CannotManage
        return item

'''class Project(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    startdate = models.DateField()
    enddate = models.DateField()

    def user_can_manage_me(self, thisuser):

        return thisuser == self.user or thisuser.has_perm('Portfolio.manage_object')

    @classmethod
    def get_manageable_object_or_404(cls, thisuser, *args, **kwds):
        item = get_object_or_404(cls, *args, **kwds)
        if not item.user_can_manage_me(thisuser):
            raise CannotManage
        return item'''
class ImageContent(models.Model):
    image = models.ImageField(default=None)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    #project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def user_can_manage_me(self, thisuser):
        return thisuser == self.user or thisuser.has_perm('Portfolio.manage_object')

    @classmethod
    def get_manageable_object_or_404(cls, thisuser, *args, **kwds):
        item = get_object_or_404(cls, *args, **kwds)
        if not item.user_can_manage_me(thisuser):
            raise CannotManage
        return item


class TextContent(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField()
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    #project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def user_can_manage_me(self, thisuser):
        return thisuser == self.user or thisuser.has_perm('Portfolio.manage_object')

    @classmethod
    def get_manageable_object_or_404(cls, thisuser, *args, **kwds):
        item = get_object_or_404(cls, *args, **kwds)
        if not item.user_can_manage_me(thisuser):
            raise CannotManage
        return item

class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def user_can_manage_me(self, thisuser):
        return thisuser == self.user or thisuser.has_perm('Portfolio.manage_object')

    @classmethod
    def get_manageable_object_or_404(cls, thisuser, *args, **kwds):
        item = get_object_or_404(cls, *args, **kwds)
        if not item.user_can_manage_me(thisuser):
            raise CannotManage
        return item

class Post(models.Model):
    title = models.CharField(max_length =30)
    content = models.CharField(max_length=400)
    date = models.DateField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def user_can_manage_me(self, thisuser):
        return thisuser == self.user or thisuser.has_perm('Portfolio.manage_object')

    @classmethod
    def get_manageable_object_or_404(cls, thisuser, *args, **kwds):
        item = get_object_or_404(cls, *args, **kwds)
        if not item.user_can_manage_me(thisuser):
            raise CannotManage
        return item


class CannotManage(Exception):
    pass