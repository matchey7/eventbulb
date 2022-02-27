from . import views
from django.urls import path

urlpatterns = [
    path('details/', views.details, name="event_details"),
    path('', views.list_of_events, name="list_of_events")
]