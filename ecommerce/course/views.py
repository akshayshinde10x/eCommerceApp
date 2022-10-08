from django.shortcuts import render, redirect
from .models import Course, Order


def home(request):
    data = Course.objects.all()
    return render(request, "home.html", {"data": data})

def buy(request):
    return render(request, "buy.html")

def placeOrder(request):
    o = Order()
    o.name = request.POST.get("name")
    o.number = request.POST.get("mobile")
    o.email = request.POST.get("email")
    o.degree = request.POST.get("degree")
    o.gradYear = request.POST.get("gradYear")

    o.save()
    return redirect("/home")