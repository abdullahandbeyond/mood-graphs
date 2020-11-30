from django.test import TestCase
from frontapp.models import *

# https://stackoverflow.com/questions/52574804/django-unit-test-for-models
# https://alcher.dev/2020/what-to-test-in-django-models/

class MoodModelTest(TestCase):
    def setUp(self):
        Mood.objects.create(name='Sad')

    def test_name_label(self):
        sad = Mood.objects.get(id=1)
        field_label = sad._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
