from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def mediapath(image):
    if image:
        return f"/media/{image}"
    return "#"
