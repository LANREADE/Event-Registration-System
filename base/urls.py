from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name="home" ),
    path('event/<str:pk>' , views.events_page , name = "event")
]