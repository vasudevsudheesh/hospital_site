from django.contrib import admin
from django.contrib import admin
from .models import Department, Doctor, Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking)
