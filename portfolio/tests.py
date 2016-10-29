from django.test import TestCase
from .models import Account

class UserTestCase(TestCase):
    def setUp(self):
        Account.objects.create(name="lion", sound="roar")
        Account.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Account.objects.get(name="lion")
        cat = Account.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')