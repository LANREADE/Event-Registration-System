from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name="home" ),
    path('user/<str:pk>/', views.user_page , name= "profile"),
    path('event/<str:pk>/' , views.events_page , name = "event"),
    path('registration-confirmation/<str:pk>/', views.registration_confirm, name = "registration-confirmation")
]