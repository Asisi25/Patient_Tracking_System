from django.contrib import admin
# from django.contrib.auth.models import AbstractUser

# Register your models here.
from .models import Patient
from .models import Appointment
from .models import MedicalHistory
from .models import Prescription
from .models import Billing
# from .models import UserAccount

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)
admin.site.register(Billing)
# admin.site.register(UserAccount)
