from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .models import Article
from .views import ArticleList


class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(link="https://wattplanner.com", user="indiana", category="Ecologie")
        Article.objects.create(link="https://wattplanner.fr", user="indiana", category="Energie")

    def test_article_list_view(self):
        """ArticleList view should return all instances of Article"""
        factory = APIRequestFactory()
        request = factory.get('/article-list/')
        view = ArticleList.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
