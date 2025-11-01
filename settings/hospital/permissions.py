from rest_framework.permissions import BasePermission

class IsNotPatientForDoctorAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            model_name = view.get_queryset().model.__name__ # добавление способа взять определенную модель с models.py
        except Exception:
            return True

        if model_name == 'Doctor':
            return getattr(request.user, 'role', None) != 'Пациент'
        return True
