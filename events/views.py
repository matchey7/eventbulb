from django.shortcuts import render
from datetime import datetime
from .models import Event
# Create your views here.

def details(request):
    return render(request, 'events/details.html')

def list(request):
    today = datetime.today()

    events = Event.objects.filter(
        datetime_gte=today).order_by("datetime")
    return render(request, 'events/list.html', {"events": events})
    