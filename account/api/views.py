from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from rest_framework import serializers

from .serializers import *

@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            newUser = serializer.save()
            token = Token.objects.get(user=newUser).key
            data = {
                "message": "New user successfully created!",
                "username": newUser.username,
                "email": newUser.email,
                "first_name": newUser.first_name,
                "last_name": newUser.last_name,
                "token": token
            }
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST',])
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(username=data["username"])
        except BaseException as e:
            raise serializers.ValidationError({"400": f'{str(e)}'})
        authUser = authenticate(request, username=data["username"], password=data["password"])
        if authUser is not None:
            login(request, authUser)
            return JsonResponse({
                "message": "Login Successful",
                "user": user.serializer(),
                "token": Token.objects.get(user=user).key
            })
        return JsonResponse({
            "message": "Invalid email/password"
        })