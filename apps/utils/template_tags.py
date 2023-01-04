from django import template
import json

register = template.Library()

@register.simple_tag(takes_context=True)
def logged_user(context):
    request = context['request']
    return json.loads(request.session['auth'])


@register.filter
def intToWeekday(value):
    weekdays = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    return weekdays[value]