from django.urls import path
from api import views

urlpatterns = [
    path('flights/', views.Flight.as_view())
]
