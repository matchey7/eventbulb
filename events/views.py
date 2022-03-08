from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Event


def details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {'event': event})


def list(request):

    filter_map = {
        'description': 'description__exact',
        'search': 'description__icontains',
        'price_min': 'cost_gte',
        'price_max': 'cost_lte',
    }

    filters = {}

    for key, value in request.GET.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value
    
    events = Event.objects.filter(**filters)
    return render(request, 'events/list.html', {'events': events})    

    # today = datetime.today()

    # events = Event.objects.filter(
    #     datetime__gte=today).order_by('datetime')
    # return render(request, 'events/list.html', {'events': events})
