from django import template

# make custome template library for view
register = template.Library()

@register.simple_tag
def my_sum(x, y):
    return x + y