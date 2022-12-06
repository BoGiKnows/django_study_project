from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'), кеширование страницы
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryList.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),

]

