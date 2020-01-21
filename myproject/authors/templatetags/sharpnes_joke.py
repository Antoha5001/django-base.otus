from django import template
from random import choice

register = template.Library()

jokes = [
'When it comes to sharpening pencils, there\'s never a dull moment.',
'There was an incident at my school today--one of the teachers caught a boy sharpening an arrowhead under his desk. She called 911, and the police got involved.',
'I tried to get into the knife sharpening academy'
]

@register.simple_tag
def joke(index=None):
    if index is None or not isinstance(index, int) or index >= len(jokes):
        return f'Не индекс {choice(jokes)}'
    else:
        return jokes[index]