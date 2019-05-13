from django.urls import path
from api import views

urlpatterns = [
<<<<<<< HEAD
    path('flights/', views.FlightGetCreate.as_view()),
    path('flights/<int:pk>', views.FlightDetail.as_view()),
    path('hotels/', views.HotelGetCreate.as_view()),
=======
    path('flights/', views.FlightList.as_view())
    path('login/', views.UserLogin),
    path('logout/', views.UserLogout),
>>>>>>> 43eaa0c40a69b6ccd8aaea5d09d9c5d1d7458dcd
]
