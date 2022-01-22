from django.urls import path

from .views import *

urlpatterns = [
    path('test', test_paginator, name='test'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('news_view/<int:news_id>/', news_view, name='news_view'),
    path('news_view/<int:pk>/', NewsView.as_view(), name='news_view'),
    # path('news/add_news/', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
]
