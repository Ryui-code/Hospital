from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from .filter import DoctorsSpecialityFilterSet
from .permissions import IsNotPatientForDoctorAccess
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = JsonResponse({'detail': 'Successfully registered.'})
        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,  # защита от JS
            secure=False,   # поставь True, если используешь HTTPS
            samesite='Lax'  # или 'Strict' для большей безопасности
        )
        return response


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        response = JsonResponse({
            'detail': 'Successfully logged in.',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })

        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,   # поставь True, если используешь HTTPS
            samesite='Lax'
        )

        return response


class LogoutView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Вы успешно вышли.'})

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsNotPatientForDoctorAccess]
    filterset_class = DoctorsSpecialityFilterSet

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentHistoryViewSet(viewsets.ModelViewSet):
    queryset = AppointmentHistory.objects.all()
    serializer_class = AppointmentHistorySerializer
    permission_classes = [IsNotPatientForDoctorAccess, IsAuthenticated]

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]