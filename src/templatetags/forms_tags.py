from django import template
from smartContract.ETHApi import API

from datetime import datetime

register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)

@register.filter
def de_hexBytes(value):
    return value.hex()

@register.simple_tag
def to_list(*args):
    return args

api = API.WebAPI()
@register.filter
def block_timestamp(block_number):
    
    block = api.get_block(block_number)
    timestamp = block['timestamp']
    date = datetime.fromtimestamp(timestamp)
    return date

@register.filter
def block_hash(block_number):
    block = api.get_block(block_number)
    sender = block['hash']
    return sender.hex()

@register.filter
def parent_hash(block_number):
    block = api.get_block(block_number)
    sender = block['parentHash']
    return sender.hex()

@register.filter
def miner(block_number):
    block = api.get_block(block_number)
    sender = block['miner']
    return sender