from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['doctor', 'patient_name', 'patient_email', 'department_name', 'appointment_date']
