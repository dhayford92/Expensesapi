from rest_framework import serializers
from .models import User



class ResgisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=40, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ('fullname', 'email', 'password')

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise ValueError({'email', ('Email already taken, Please try again')})
        return attrs

    def perform_create(self, validata):
        return User.objects.create_user(**validata)



class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=40, write_only=True)
    class Meta:
        model = User
        fields = ('fullname', 'email', 'password', 'tokens')
        read_only_fields = ['fullname', 'tokens']
