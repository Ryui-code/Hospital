from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('Врач', 'Врач'),
    ('Пациент', 'Пациент'),
)

SPECIALITY_CHOICES = (
    ('Врач', 'Врач'),
    ('Онколог', 'Онколог'),
    ('Фармацевт', 'Фармацевт'),
    ('Хирург', 'Хирург'),
    ('Аллерголог', 'Аллерголог'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=STATUS_CHOICES)
    data_registered = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

class Doctor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)])
    birth_day = models.DateField()
    phone_number = PhoneNumberField()
    speciality = models.CharField(max_length=20, choices=SPECIALITY_CHOICES)

    def __str__(self):
        return self.full_name

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    doctors_speciality = models.CharField(max_length=20, choices=SPECIALITY_CHOICES)
    text = models.TextField(default='<Напишите причину>')
    time = models.DateTimeField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.full_name

class AppointmentHistory(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '><'

class Bill(models.Model):
    patient = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    bill = models.SmallIntegerField()

    def __str__(self):
         return self.bill