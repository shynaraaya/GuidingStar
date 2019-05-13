from django.urls import path
from api import views

urlpatterns = [
    path('flights/', views.FlightGetCreate.as_view()),
    path('flights/<int:pk>', views.FlightDetail.as_view()),
    path('hotels/', views.HotelGetCreate.as_view()),
]
