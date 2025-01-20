from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Patient
from .serializers import UserSerializer, LoginSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DoctorCreateView(generics.CreateAPIView):
    queryset = User.objects.filter(is_doctor=True)
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        # Generate token
        refresh = RefreshToken.for_user(user)
        appointments = []  # Replace with actual appointment fetching logic

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'Successfully logged in',
            'appointments': appointments,
        }, status=status.HTTP_200_OK)
