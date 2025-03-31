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
            username = models.Relog.objects.create(username = username, email = email, password = password)
            username.save()
            return redirect("login")
    return render(request, "register.html")

def login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        obj_user = models.Relog.objects.filter(username=username, password=password)

        if obj_user:
            return redirect('dashboard')
        
        error_mssg = "User not found"
        return render(request, "login.html", {"error_mssg":error_mssg})
    return render(request, "login.html")

