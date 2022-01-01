from django.shortcuts import render, get_object_or_404
from news.models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Cписок новостей',
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)


def news_view(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_view.html', {"news": news})
