"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from guestbook.models import Greeting

class SimpleTest(TestCase):
    def setUp(self):
        Greeting(content='This is a test greeting').save()

        def test_setup(self):
        self.assertEqual(1, len(Greeting.objects.all()))
        self.assertEqual('This is a test greeting', Greeting.objects.all()[0].content)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

