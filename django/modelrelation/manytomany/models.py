from django.db import models

# M : N
# 1. Doctor : Patient (1:N)
# 2. Doctor : Reservation : Patient (1:N + 1:N)
# 3. Doctor : Patient (M : N)
# 4. Doctor : Patient (N : M)
class Doctor(models.Model):
    name = models.CharField(max_length = 20)


class Patient(models.Model):
    name = models.CharField(max_length = 20)
    # doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    # doctors = models.ManyToManyField(Doctor, through = 'Reservation')
    doctors = models.ManyToManyField(Doctor)

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete = models.CASCADE)