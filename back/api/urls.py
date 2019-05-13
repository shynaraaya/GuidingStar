from django.urls import path
from api import views

urlpatterns = [
    path('flights/', views.FlightList.as_view())
    path('login/', views.UserLogin),
    path('logout/', views.UserLogout),
]
