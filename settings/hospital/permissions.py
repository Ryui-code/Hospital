from rest_framework.permissions import BasePermission

class IsNotPatientForDoctorAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            model_name = view.get_queryset().model.__name__ # добавление способа взять определенную модель с models.py
        except Exception:
            return True

        if model_name in ['Doctor', 'AppointmentHistory', 'Bill']: # объект который мы используем
            return getattr(request.user, 'role', None) != 'Пациент' # не возвращать пользователя с ролью 'Пациент'
        return True # возвращать пользователя если выбранная роль другая