from django.urls import path
from api import views

urlpatterns = [
	path('hotels/', views.hotel_lists),
	path('hotels/<int:pk>/', views.hotel_list_detail),
	path('hotels/<int:pk>/hotel/', views.hotel),
    path('flights/', views.flight),
    path('flights/<int:pk>', views.flights_list_detail),
    path('flights/<int:pk>/flight', views.flight_lists)
]
