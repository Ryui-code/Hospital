from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'doctor', DoctorViewSet, basename='doctor')
router.register(r'appointment', AppointmentViewSet, basename='appointment')
router.register(r'appointment_history', AppointmentHistoryViewSet, basename='appointment_history')
router.register(r'bill', BillViewSet, basename='bill')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls))
]