from django import template
from django.urls import reverse, resolve, Resolver404
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    try:
        resolved_url = resolve(current_url).url_name
    except:
        resolved_url = ''

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related("parent")

    active_items = []
    for item in menu_items:
        if item.get_url() == current_url or (item.named_url and item.named_url == resolved_url):
            active_items.append(item.id)
            parent = item.parent
            while parent:
                active_items.append(parent.id)
                parent = parent.parent

    return {
        "menu_items": menu_items,
        "active_items": active_items,
        "menu_name": menu_name,
        "request": context['request'],
    }