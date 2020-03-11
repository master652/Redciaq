from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def home(request):
    return render(request,"StationAdministrator/index.html")
def logout_request(request):
    logout(request)
    return redirect("/AdminLogin")

