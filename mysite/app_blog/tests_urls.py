from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView
from .models import Article
# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles_category_list', args= ('name',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_news_detail_view(self):
        url = reverse('news_detail', args=[2024, 10, 5, 'test-article'])
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 404])
