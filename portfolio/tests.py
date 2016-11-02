from django.test import TestCase
from .models import Portfolio

class URLTestCase(TestCase):
    def setUp(self):
        return


    def test_index(self):

            resp = self.client.get('/portfolio/')
            self.assertEqual(resp.status_code, 200)


    def test_login(self):

            resp = self.client.get('/login/')
            self.assertEqual(resp.status_code, 200)


    def test_register(self):
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)



class ViewsTestCase(TestCase):
    def test_portfolio(self):
        resp = self.client.get('/portfolio/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_poll_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])