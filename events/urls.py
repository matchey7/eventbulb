from . import views
from django.urls import path

urlpatterns = [
    path('details/', views.details, name="event_details"),
    path('', views.events_list, name="events_list")
]