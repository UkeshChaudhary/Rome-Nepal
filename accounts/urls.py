from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('verify/', VerifyOTP.as_view()),
    path('login/', LoginView.as_view(), name='login'),
]