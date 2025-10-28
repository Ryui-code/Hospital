from django_filters import FilterSet
from .models import Doctor

class DoctorsSpecialityFilterSet(FilterSet):
    class Meta:
        model = Doctor
        fields = [
            'speciality',
            'full_name',
        ]