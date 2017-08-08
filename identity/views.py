from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"identity/index.html")

def logindialog(request):
    return render(request,"identity/dashboard.html",{})

def dashboard(request):
    return render(request,"identity/dashboard.html")

def userprofile(request):
    return render(request,"identity/user.html")

