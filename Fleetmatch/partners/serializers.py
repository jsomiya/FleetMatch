from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Registration

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Signup Serializer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('first_name','last_name','company_id','company_name','mobile_number','services','description')