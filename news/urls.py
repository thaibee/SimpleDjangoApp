from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('catagory/<int:category_id>/', get_category, name='category'),
    path('news_view/<int:news_id>/', news_view, name='news_view'),
]
