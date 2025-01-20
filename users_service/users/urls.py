from django.urls import path
from .views import UserCreateView, DoctorCreateView, LoginView

urlpatterns = [
    path('register/patient/', UserCreateView.as_view(), name='register-patient'),
    path('register/doctor/', DoctorCreateView.as_view(), name='register-doctor'),
    path('login/', LoginView.as_view(), name='login'),
]
