from rest_framework import serializers
from .models import *
from Trip.serializers import TripSerializer


class UserSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many = True, read_only=True)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'is_verified', 'trips']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


# Verify Account

class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


#Login 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)