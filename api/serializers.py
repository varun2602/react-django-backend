from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import models

class LoginSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)
        token["role"] = user.role
        return token
    

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = models.CustomUser 
        fields = ["id", "username","email", "password", "password2", "role"] 

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords dont match")
        return attrs
        
    def create(self, validated_data):
        user = models.CustomUser.objects.create(username = validated_data["username"], email = validated_data["email"], role = validated_data["role"])
        user.set_password(validated_data["password"])
        user.save()
        return user


    