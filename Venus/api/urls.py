from django.urls import path
from .views import get_article_by_id, add_article

urlpatterns = [
    path('article/<int:id>/', get_article_by_id, name='get_article_by_id'),
    path('add-article/', add_article, name='add_article'),
]
