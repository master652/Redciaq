from django.urls import path
from apps.login import views

urlpatterns = [
    path('',views.Login.as_view(),name="login"),
    path('AdminRegister',views.Register.as_view(),name="register"),
]