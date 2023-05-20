from django.shortcuts import render, redirect
from .models import Department, Doctor
from .forms import BookingForm


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def departments(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def booking_success(request):
    return render(request, 'booking_success.html')
