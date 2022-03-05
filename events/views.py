from django.shortcuts import render
from datetime import datetime
from .models import Event
# Create your views here.

def details(request):
    return render(request, 'events/details.html')

def events_list(request):
    events = Event.objects.all()
    return render(request, 'events/events_list.html', {"events": events})