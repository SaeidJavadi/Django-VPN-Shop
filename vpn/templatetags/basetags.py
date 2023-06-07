from django import template
import math
import jdatetime

register = template.Library()


@register.filter()
def daytomo(value):
    return math.ceil(value / 31)


@register.filter()
def tocurrencys(value):
    return str("{:,}".format(int(value)))
