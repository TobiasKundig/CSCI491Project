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




class ModelsViewsTestCase(TestCase):

    #below is an example test case for adding data to a test database and running the application.
    #django won't run data against a real database.

    '''class PollsViewsTestCase(TestCase):
    fixtures = ['polls_views_testdata.json']

    def test_index(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_poll_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])
        poll_1 = resp.context['latest_poll_list'][0]
        self.assertEqual(poll_1.question, 'Are you learning about testing in Django?')
        self.assertEqual(poll_1.choice_set.count(), 2)
        choices = poll_1.choice_set.all()
        self.assertEqual(choices[0].choice, 'Yes')
        self.assertEqual(choices[0].votes, 1)
        self.assertEqual(choices[1].choice, 'No')
        self.assertEqual(choices[1].votes, 0)'''