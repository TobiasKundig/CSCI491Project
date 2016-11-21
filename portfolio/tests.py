
from django.test import TestCase, RequestFactory, Client
from .models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.core.files.images import *
from .views import *
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login, authenticate, logout

from io import BytesIO
from PIL import Image


class URLTestCase(TestCase):
    def setUp(self):
        #, the RequestFactory provides a way to generate a request instance that can be used as the first argument to any view.
        self.factory = RequestFactory()

        #create a user and portfolio
        self.user =User.objects.create_user(username="testuser1",email="mdolan2424@gmail.com",password="test1234")

        '''user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    header = models.CharField(max_length=150)
    style = models.CharField(max_length=30)
    img = '''
    def test_index(self):
            resp = self.client.get('/')
            self.assertEqual(resp.status_code, 200)

    def test_contact(self):
        resp = self.client.get('/contact')

    def test_login(self):
            resp = self.client.get('/login/')
            self.assertEqual(resp.status_code, 200)

    def test_register(self):
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)


    #assumes the user is logged in
    def test_profile(self):
        request = self.factory.get('/profile/')

        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(150, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'

        img = ImageFile(file)

        Portfolio.objects.create(user=self.user, name="This is a test portfolio name", header="testheader",
                                 style="dark", img=img)
        request.user = self.user
        resp = profile(request)
        self.assertEqual(resp.status_code, 200)

    def test_profile_name(self):



        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(150, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'

        img = ImageFile(file)

        Portfolio.objects.create(user=self.user, name="This is a test portfolio name", header="testheader",
                                 style="dark", img=img)
        resp = self.client.get('/testuser1/')


        self.assertEqual(resp.status_code, 200)

    def test_profile_edit(self):



        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(150, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'

        img = ImageFile(file)

        Portfolio.objects.create(user=self.user, name="This is a test portfolio name", header="testheader",
                                 style="dark", img=img)



        resp = self.client.get('/testuser1/edit/')

        self.assertEqual(resp.status_code, 200)
    '''def test_profile_images(self):
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)

    def test_profile_project_new(self):
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)'''



'''url(r'^$', views.index, name='index'),
    url(r'^contact/$',  views.contact, name='contact'),
    url(r'^register/$', RegisterView.as_view(), name='register'), #registration page
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'), #the logged in users own profile
    url(r'^(?P<user>[\w\-]+)/$', views.detail, name='detail'),
    url(r'^(?P<user>[\w\-]+)/images/$', ImageManagementView.as_view(), name='image_listing'), #the logged in users own profile
    url(r'^(?P<user>[\w\-]+)/edit/$', PortfolioUpdate.as_view(), name='portfolio_update'),
    url(r'^(?P<user>[\w\-]+)/project/new/$', ProjectCreate.as_view(), name='project_create'),
]'''
