from django.test import SimpleTestCase
from django.urls import reverse, resolve
from frontapp.views import list_view, create_view

class TestUrls(SimpleTestCase):

    def test_list_url(self):
        url = reverse('list_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func, list_view)

    def test_add_url(self):
        url = reverse('create_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func, create_view)
