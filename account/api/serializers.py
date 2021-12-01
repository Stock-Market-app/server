from rest_framework import serializers
from ..models import *

class RegisterSerializer(serializers.ModelSerializer):
    confirmPass = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'confirmPass']
        extra_kwargs = {
            'password': {'write_only': True}  
        }
    def save(self):
        if len(User.objects.filter(email=self.validated_data['email'])) > 0:
            raise serializers.ValidationError({"error": "email already taken!"})
        newUser = User(
            username=self.validated_data['email'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        if self.validated_data['password'] != self.validated_data['confirmPass']:
            raise serializers.ValidationError({"error": "Passwords Must match!"})
        newUser.set_password(self.validated_data['password'])
        newUser.save()
        return newUser
