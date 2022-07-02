from django import template

register = template.Library()

def short_content(value):
    return value[:500] + ' .....'

register.filter('short_content', short_content)