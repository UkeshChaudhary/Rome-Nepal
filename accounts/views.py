from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .emails import *


# Create your views here.


# Register API

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                        'message' : 'Registration is Sucessfully done.',
                        'data' : serializer.data,
                }, status=status.HTTP_200_OK)
            return Response({
                'message' : 'Something went wrong',
                'data' : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)



# Verify Email

class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)


            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email = email)
                if not user.exists():
                    return Response({
                        'message' : 'Something went wrong',
                        'data' : 'invalid email'
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                if not user[0].otp == otp:
                    return Response({
                        'message' : 'Something went wrong',
                        'data' : 'wrong otp'
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                user = user.first()
                user.is_verified = True
                user.save()

                return Response({
                    'message' : 'account Verified',
                    'data' : {}
                }, status=status.HTTP_201_CREATED) 

            return Response({
                'message' : 'Something went wrong',
                'data' : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)  

                
        except Exception as e:
            print(e)


# Login View
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_verified:
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
                return Response({'error': 'Email not verified'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)