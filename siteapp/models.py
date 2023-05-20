from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')  # Specify the upload directory for the image field

    # Add more fields as per your requirements

    def __str__(self):
        return f"{self.name} - {self.specialization}"


from django.db import models


class Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()  # Use EmailField for email input
    department_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    # Add more fields as per your requirements

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"
