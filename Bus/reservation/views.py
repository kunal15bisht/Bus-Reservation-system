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
    context = {
        "bus": [],
        "error_mssg": ""
    }

    if request.method == "GET":
        source = request.POST.get('from', '').strip().upper()
        destination = request.POST.get('to', '').strip().upper()
        departure_date = request.POST.get('date', '').strip()

        if source and destination and departure_date:
            bus_list = models.Bus.objects.filter(
                source=source,
                destination=destination,
                departure_date=departure_date
            )
            if bus_list.exists():
                context["bus"] = bus_list
            else:
                context["error_mssg"] = "Result: Not Found"
        else:
            context["error_mssg"] = "Please fill all the fields."

    return render(request, "dashboard.html", context)


def book(request,id):
    email = request.session['email']
    bus = models.Bus.objects.get(id=id)
    user = models.User.objects.get(email=email)

    if bus:
        return render(request, "booking.html", {"bus":bus,"user":user})
    return redirect('dashboard')

def pay(request):
    if request.method == 'POST':
        raw_time = request.POST.get('time')  # e.g., "6:18 AM"

        try:
            departure_time = datetime.strptime(raw_time.strip(), "%I:%M %p").time()
        except (ValueError, AttributeError):
            # Fallback or error message
            return redirect('error_page')
        models.Reservation.objects.create(
            username=request.POST.get('user'),
            email=request.POST.get('email'),
            bus_name=request.POST.get('bus_name'),
            bus_number=request.POST.get('bus_number'),
            source=request.POST.get('from'),
            destination=request.POST.get('to'),
            departure_time=request.POST.get('date'),
            time=departure_time,
            No_of_person=request.POST.get('No_of_person'),
            total_amount=request.POST.get('amount')
        )
        return redirect('dashboard')  # Replace with your actual success URL or page

    return redirect('booking')

def mybooking(request):
    email = request.session['email']
    bus = models.Reservation.objects.filter(email = email)
    if bus:
        return render(request,"mybooking.html",{"bus":bus})
    error_mssg = "No Data"
    return render(request, "mybooking.html", {"error_mssg": error_mssg})

def delete(request, id):
    data =models.Reservation.objects.get(id=id)
    if data:
        data.delete()
        return redirect('mybooking')
    error_mssg = "No Data"
    return render(request, "mybooking.html", {"error_mssg": error_mssg})
    