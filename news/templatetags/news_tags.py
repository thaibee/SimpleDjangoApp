from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(qty=Count('news')).filter(qty__gt=0)
    return {"categories": categories, }
