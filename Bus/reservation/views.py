from datetime import datetime
from django.shortcuts import render, redirect
from reservation import models

def register(request):
    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_list = models.User.objects.filter(username = username)
        error_mssg =[]
        if user_list:
            error_mssg = "User name is already exist"
            return render(request, "register.html", {"error_mssg":error_mssg})
        else:
            username = models.User.objects.create(username = username, email = email, password = password)
            username.save()
            return redirect("login")
    return render(request, "register.html")

def login(request):
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        obj_user = models.User.objects.filter(email=email, password=password)

        if obj_user:
            request.session['email'] = email
            request.session.set_expiry(None)
            request.session['pass'] = password 
            request.session.set_expiry(None)
            return redirect('dashboard')
        
        error_mssg = "User not found"
        return render(request, "login.html", {"error_mssg":error_mssg})
    return render(request, "login.html")

def dashboard(request):
    bus = models.Bus.objects.all()
    if bus:
        return render(request,"dashboard.html",{"bus":bus})
    error_mssg = "No Data"
    return render(request, "dashboard.html", {"error_mssg": error_mssg})

def search(request):
    if request.method == "POST":
        source = request.POST.get('from').upper()
        destination = request.POST.get('to').upper()
        departure_date = request.POST.get('date')
        
        bus_list = models.Bus.objects.filter(source=source, destination=destination, departure_date=departure_date)
               
        if bus_list:
            return render(request, "dashboard.html", {"bus": bus_list})
        error_mssg = "Result: Not Found"
        return render(request, "dashboard.html", {"error_mssg": error_mssg})
        
    return render(request, "dashboard.html")



