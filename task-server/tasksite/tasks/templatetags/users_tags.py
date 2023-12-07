from django import template
from users.models import *

register = template.Library()

@register.inclusion_tag('tasks/list_users.html')
def show_users():
    return {'users': User.objects.all()}