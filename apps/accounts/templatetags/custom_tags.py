# -*- coding: UTF-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 替换换行符
@register.simple_tag
def format_str(string):
    return mark_safe(string.replace(',', '<br/>'))
