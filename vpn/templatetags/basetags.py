from django import template
import math

register = template.Library()


@register.filter()
def daytomo(value):
    return math.ceil(value / 31)
