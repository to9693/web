from django.db import models

# M : N
# 1. Doctor : Patient (1:N)
# 2. Doctor : Reservation : Patient (1:N + 1:N)
# 3. Doctor : Patient (M : N) (Reservation 사용)
# 4. Doctor : Patient (N : M)
class Doctor(models.Model):
    name = models.CharField(max_length = 20)


class Patient(models.Model):
    name = models.CharField(max_length = 20)
    # doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    # 이걸 사용해야함  doctors = models.ManyToManyField(Doctor, through = 'Reservation')
    doctors = models.ManyToManyField(Doctor, related_name = 'patients') #

# 이것도 class Reservation(models.Model):
# 이것도 doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
# 이것도 patient = models.ForeignKey(Patient, on_delete = models.CASCADE)