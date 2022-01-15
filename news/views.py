from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm2
from django.urls import reverse_lazy


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class NewsView(DetailView):
    model = News
    template_name = 'news/news_view.html'
    context_object_name = 'news'


class CreateNews(CreateView):
    form_class = NewsForm2
    template_name = 'news/add_news.html'
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
