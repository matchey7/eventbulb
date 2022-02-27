from django.shortcuts import render

# Create your views here.

def details(request):
    return render(request, 'events/details.html')

def list_of_events(request):
    return render(request, 'events/list_of_events.html')