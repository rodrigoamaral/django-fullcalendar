===================
django-fullcalendar
===================

FullCalendar_ integration with Django. Provides a model representing a FullCalendar Event object and some template tags to wrap the Javascript code needed to integrate FullCalendar to Django Templates.

**WARNING:** This project is currently in pre-alpha. Use it at your own risk!

Installation
------------

Since this package is not available on PyPI yet, you can install it directly from this repo by doing:

::

  $ pip install -e git+https://github.com/rodrigoamaral/django-fullcalendar.git#egg=django-fullcalendar

Configuration
-------------

Add the ``fullcalendar`` module to the INSTALLED_APPS of your Django project ``settings.py``, like this:

::

  INSTALLED_APPS = (
    # other installed apps here
    # (...)
    'fullcalendar',
  )
  
django-fullcalendar now gets FullCalendar_ javascript and CSS dependency files from its respective CDNs by default. If you need to get them from a different place, you must inform it in your ``settings.py``:

::

  FULLCALENDAR = {
      'css_url': <path_or_url_to_css_file>,
      'print_css_url': <path_or_url_to_print_css_file>,
      'javascript_url': <path_or_url_to_javascript_file>,
      'jquery_url': <path_or_url_to_jquery_file>,
      'jquery_ui_url': <path_or_url_to_jquery_ui_file>,
  }

Usage
-----

Your templates should basically look something like this:

::

  {% load fullcalendar_tags %}

  <!DOCTYPE html>
  <head>    

      <title></title>

      {% fullcalendar_css %} 
      {% fullcalendar_print_css %} 
      {% fullcalendar_jquery %}
      {% fullcalendar_jquery_ui %} 
      {% fullcalendar_javascript %}
        
      {% calendar_init event_url %}

  </head>
  (...)

Then, place the calendar template tag where you want the calendar to appear:

::
  
  {% calendar %}

For more details, please refer to the ``demo`` application source code.

Requirements
------------

django-fullcalendar was originally developed to work with:

- Python 2.7
- Django 1.6
- FullCalendar 1.6.4

Bugs and requests
-----------------

Please feel free to fork this repo or open issues_ for bug reporting and other stuff that may be missing.

.. _FullCalendar: http://arshaw.com/fullcalendar/
.. _issues: http://github.com/rodrigoamaral/django-fullcalendar/issues
