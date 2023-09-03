from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.urls import reverse
# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_absolute_url(self):
            return reverse('patient_tracking:patients-detail', args=[self.pk])

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.patient} on {self.appointment_date}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    diagnosis_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Medical history of {self.patient} - {self.condition}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)
    prescription_date = models.DateField(default=timezone.now)
    medication = models.TextField()
    dosage = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription for {self.patient.first_name} {self.patient.last_name}"


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bill_date = models.DateField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially Paid'),
        ('cancelled', 'Cancelled'),
    ))

    def __str__(self):
        return f"Billing for {self.patient.first_name} {self.patient.last_name}"


# class UserAccount(AbstractUser):
#     ROLES = (
#         ('doctor', 'Doctor'),
#         ('nurse', 'Nurse'),
#         ('admin', 'Administrator'),
#         # Add more roles as needed
#     )
#     role = models.CharField(max_length=20, choices=ROLES)

#     def __str__(self):
#         return f"{self.username} ({self.get_role_display()})"
    
#     class Meta:
#         # Add the following line to set a related_name for user_permissions
#         permissions = [
#             ("can_view_patients", "Can view patients"),
#             ("can_manage_appointments", "Can manage appointments"),
#             # Define more permissions as needed
#         ]