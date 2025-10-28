from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


@admin.register(CustomUser)
class RegistrationAdmin(UserAdmin):
    fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password', 'email', 'first_name', 'last_name',
                'phone', 'country', 'token', 'data_registered'
            ),
        }),
    ]
    readonly_fields = ['token', 'data_registered']

admin.site.register(Appointment)
admin.site.register(AppointmentHistory)
admin.site.register(Bill)
admin.site.register(Doctor)