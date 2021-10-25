from django import template

register = template.Library()

@register.filter
def de_hexBytes(value):
    return value.decode('utf-8').encode('ascii', errors=ignores)