from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Donation, UserProfile


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, role=role)
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


def dashboard(request):
    donations = Donation.objects.filter(donor=request.user)
    return render(request, 'dashboard.html', {'donations': donations})


# ---------- DONATION CATEGORY PAGES ----------

def food_donate(request):
    if request.method == "POST":
        Donation.objects.create(
            donor=request.user,
            category="Food",
            sub_type=request.POST['food_type'],   # Rice, Wheat, Cooked food, etc.
            quantity=request.POST['quantity'],
            location=request.POST['location'],
            contact=request.POST['contact'],
            date=request.POST['date']
        )
        return redirect('dashboard')

    return render(request, 'donate_food.html')


def blood_donate(request):
    if request.method == "POST":
        Donation.objects.create(
            donor=request.user,
            category="Blood",
            sub_type=request.POST['blood_group'],   # A+, B+, O-, etc.
            quantity=request.POST['quantity'],
            location=request.POST['location'],
            contact=request.POST['contact'],
            date=request.POST['date']
        )
        return redirect('dashboard')

    return render(request, 'donate_blood.html')


def clothes_donate(request):
    if request.method == "POST":
        Donation.objects.create(
            donor=request.user,
            category="Clothes",
            sub_type=request.POST['clothes_type'],  # Shirt, Pants, Kids wear, etc.
            quantity=request.POST['quantity'],
            location=request.POST['location'],
            contact=request.POST['contact'],
            date=request.POST['date']
        )
        return redirect('dashboard')

    return render(request, 'donate_clothes.html')


def books_donate(request):
    if request.method == "POST":
        Donation.objects.create(
            donor=request.user,
            category="Books",
            sub_type=request.POST['book_type'],   # Engineering, School, Novels, etc.
            quantity=request.POST['quantity'],
            location=request.POST['location'],
            contact=request.POST['contact'],
            date=request.POST['date']
        )
        return redirect('dashboard')

    return render(request, 'donate_books.html')

def donate(request):
    return render(request, 'donate.html')
