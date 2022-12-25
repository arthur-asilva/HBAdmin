from django import template
from apps.users.models import Administrator
import json

register = template.Library()

@register.simple_tag(takes_context=True)
def logged_user(context):
    request = context['request']
    return json.loads(request.session['auth'])
    