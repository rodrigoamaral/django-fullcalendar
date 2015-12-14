from django import template
from django.utils.safestring import mark_safe
from ..fullcalendar import css_url, print_css_url, javascript_url, jquery_url, jquery_ui_url

register = template.Library()


@register.inclusion_tag("fullcalendar/calendar.html")
def calendar():
    return {}

@register.inclusion_tag("fullcalendar/calendar_init.html")
def calendar_init(calendar_config_options):
    return {'calendar_config_options': mark_safe(calendar_config_options)}

@register.simple_tag
def fullcalendar_css_url():
    return css_url()

@register.simple_tag
def fullcalendar_print_css_url():
    return print_css_url()

@register.simple_tag
def fullcalendar_javascript_url():
    return javascript_url()

@register.simple_tag
def fullcalendar_jquery_url():
    return jquery_url()

@register.simple_tag
def fullcalendar_jquery_ui_url():
    return jquery_ui_url()

@register.simple_tag
def fullcalendar_css():
    url = fullcalendar_css_url()
    return mark_safe("<link href='%s' rel='stylesheet' />" % url)

@register.simple_tag
def fullcalendar_print_css():
    url = fullcalendar_print_css_url()
    return mark_safe("<link href='%s' rel='stylesheet' media='print' />" % url)

@register.simple_tag
def fullcalendar_jquery():
    url = fullcalendar_jquery_url()
    return mark_safe("<script src='%s'></script>" % url)

@register.simple_tag
def fullcalendar_jquery_ui():
    url = fullcalendar_jquery_ui_url()
    return mark_safe("<script src='%s'></script>" % url)

@register.simple_tag
def fullcalendar_javascript():
    url = fullcalendar_javascript_url()
    return mark_safe("<script src='%s'></script>" % url)
