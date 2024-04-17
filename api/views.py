from django.shortcuts import render, HttpResponse
from rest_framework import generics 
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt
from . import serializers
from . import models

class LoginUser(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer

@csrf_exempt
def test(request):
    print(request)


class RegisterUser(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.RegisterSerializer
    
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    return HttpResponse("Successful")
