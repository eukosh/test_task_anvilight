from django import template
from ..models import Category
import itertools


register = template.Library()


def get_category(form):
    return form.initial['category_id']


@register.simple_tag
def group_by_category(forms):
    res = [(Category.objects.get(id=k), list(g)) for k, g in itertools.groupby(forms, key=get_category)]
    return res
