from rest_framework.permissions import BasePermission

class IsNotPatientForDoctorAccess(BasePermission):

    def has_permission(self, request, view):
        if getattr(view, 'queryset', None) and view.queryset.model.__name__ == 'Doctor':
            user = request.user
            return getattr(user, 'role', None) != 'Пациент'
        return True

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated