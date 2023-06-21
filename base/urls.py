from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name="home" ),
    path('login/', views.login , name = 'login'),
    path('register/', views.register , name = 'register'),
    path('user/<str:pk>/', views.user_page , name= "profile"),
    path('event/<str:pk>/' , views.events_page , name = "event"),
    path('registration-confirmation/<str:pk>/', views.registration_confirm, name = "registration-confirmation"),
    path('account/' , views.account_page, name = "account"),
    path('project_submission/<str:pk>', views.project_submission, name ='project-submision'),
    path('update-submission/<str:pk>/' , views.update_submission , name ="update-submission")
]