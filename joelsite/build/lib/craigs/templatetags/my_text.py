from django import template

register = template.Library()

@register.filter
def replace_space(string):
    string = string.replace(' ', '.')
    return string.replace('+', '.')


@register.filter
def replace_plus(string):
    return string.replace('+', ' ')