from .models import Appointment
from modeltranslation.translator import TranslationOptions, register

@register(Appointment)
class AppointmentTranslationOptions(TranslationOptions):
    fields = ('text',)