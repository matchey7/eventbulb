from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name="events_list"),
    path('<int:id>/', views.details, name="events_details"),
]
