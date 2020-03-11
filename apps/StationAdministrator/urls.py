from django.urls import path
from apps.StationAdministrator import views

urlpatterns = [
    path('',views.home,name="home"),
    path('Salir',views.logout_request,name="Salir"),
]