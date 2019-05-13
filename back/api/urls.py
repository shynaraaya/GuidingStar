from django.urls import path
from api import views

urlpatterns = [

    path('flights/', views.FlightGetCreate.as_view()),
    path('flights/<int:pk>', views.FlightDetail.as_view()),
    path('hotels/', views.HotelGetCreate.as_view()),
    path('hotels/<int:pk>', views.HotelDetail.as_view()),
    path('reviews/', views.ReviewGetCreate.as_view()),
    path('reviews/<int:pk>', views.ReviewRetrieve.as_view()),
    path('login/', views.UserLogin),
    path('logout/', views.UserLogout),
]
