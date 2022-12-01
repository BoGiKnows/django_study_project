from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryList.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]

