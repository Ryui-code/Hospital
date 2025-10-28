from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .filter import DoctorsSpecialityFilterSet
from .permissions import IsAuthenticated, IsNotPatientForDoctorAccess
from .serializers import *


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        user = serializer.save()
        return Response({'detail': 'Successfully registered.', 'token': user.token})

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_excepions=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'token': user.token
        })

class LogoutView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
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