from django import template

register = template.Library()

@register.filter()
def model_name(obj):
    try:
        return obj._meta.model.__name__
    except AttributeError:
        return None
    
