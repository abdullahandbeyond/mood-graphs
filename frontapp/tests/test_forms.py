from django.test import TestCase
from frontapp.forms import TrackingForm

# https://adamj.eu/tech/2020/06/15/how-to-unit-test-a-django-form/
# https://micropyramid.com/blog/django-unit-test-cases-with-forms-and-views/

class TestForms(TestCase):
    def test_tracking_form(self):
        form_data = {'something', 'something'}
        form = TrackingForm(data = form_data)
        self.assertTrue(form.is_valid())
