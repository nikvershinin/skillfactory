from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag()
def show_cats(format_string='%b %d %Y'):
   return datetime.utcnow().strftime(format_string)