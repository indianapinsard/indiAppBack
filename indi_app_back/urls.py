from django.contrib import admin
from django.urls import path
from indi.views import ArticleList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article-list/', ArticleList.as_view(), name='article_list'),
]
