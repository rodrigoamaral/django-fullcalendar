from django.shortcuts import render
from django.http import HttpResponse
from fullcalendar.models import CalendarEvent
from fullcalendar.util import events_to_json


def index(request):
    event_url = 'all_events/'
    return render(request, 'demo/index.html', {'event_url': event_url})

def all_events(request):
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')