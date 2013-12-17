from django.conf import settings

# django-fullcalendar static file location defaults to FullCalendar default 
# folder structure, expected to be under the STATIC_URL

FULLCALENDAR_DEFAULTS = {
    'css_url': '/fullcalendar/js/fullcalendar/fullcalendar.css',
    'javascript_url': '/fullcalendar/js/fullcalendar/fullcalendar.js',
    'jquery_url': '/fullcalendar/js/lib/jquery.min.js',
    'jquery_ui_url': '/fullcalendar/js/lib/jquery-ui.custom.min.js',
}

# Updates location based on configuration defined by 
# settings.py of the project

FULLCALENDAR = FULLCALENDAR_DEFAULTS.copy()
FULLCALENDAR.update(getattr(settings, 'FULLCALENDAR', {}))

def css_url():
    return settings.STATIC_URL + FULLCALENDAR['css_url']

def javascript_url():
    return settings.STATIC_URL + FULLCALENDAR['javascript_url']

def jquery_url():
    return settings.STATIC_URL + FULLCALENDAR['jquery_url']

def jquery_ui_url():
    return settings.STATIC_URL + FULLCALENDAR['jquery_ui_url']
