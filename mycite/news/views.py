from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

from .models import News, Category


def index(request: HttpRequest):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'список новостей',
        'categories': categories,
    }
    return render(request, 'news/index.html', context)


def get_category(request: HttpRequest, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': "Список новостей",
        'category': category,
        'categories': categories,
    }

    return render(request, template_name='news/category.html', context=context)


def test(request: HttpRequest):
    return HttpResponse('<h1>Как ты меня задолбал</h1>')
