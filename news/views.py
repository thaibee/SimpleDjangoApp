from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm2
from django.urls import reverse_lazy
from .utils import MyMixin


def test_paginator(request):
    test_list = ['1asdf', '2gasd', '3asgsag', '4asdg', '5sga', '6asgd', '7sadg', '8sag', '9sg']
    paginator = Paginator(test_list, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test_paginator.html', {'page_obj': page_obj})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    mixin_prop = 'Hello world'
    paginate_by = 2

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class NewsView(DetailView):
    model = News
    template_name = 'news/news_view.html'
    context_object_name = 'news'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm2
    template_name = 'news/add_news.html'
    login_url = '/admin/'
    redirect_field_name = None
    # success_url = reverse_lazy('home')

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Cписок новостей',
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context)


# def news_view(request, news_id):
#     news = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/news_view.html', {"news": news})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm2(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm2()
#     return render(request, 'news/add_news.html', {'form': form})
