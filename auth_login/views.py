from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import generics, serializers, status
from rest_framework.response import Response


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user = User.objects.get(username =request.data.get('username') )
        get_user = profile.objects.get(user=user)
        get_user.user_Category = request.data.get('user_category')

        return Response({'status':'created'},status=status.HTTP_201_CREATED)