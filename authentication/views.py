from django.shortcuts import render
from .models import User
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status, response



class ResgisterApiView(generics.GenericAPIView):
    serializer_class = ResgisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = authenticate(email=email, password=password)
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': 'Invalid Credentail'}, status=status.HTTP_401_UNAUTHORIZED)