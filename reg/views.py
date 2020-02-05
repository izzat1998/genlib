import random

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from reg.models import CustomUser
from django.core.mail import send_mail


class UserRegister(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = request.data.get('username')
        password = request.data.get("password")

        if first_name is None or last_name is None:
            return Response({'error': 'Please provide first_name or last_name'}, status=HTTP_400_BAD_REQUEST)
        if not username:
            return Response({'error': 'Please provide username'}, status=HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.create(first_name=first_name, last_name=last_name, username=username,
                                         password=password)
        token = Token.objects.create(user=user)
        return Response({'username': user.username,
                         'password': user.password,
                         'token': token.key}, status=HTTP_200_OK, )


class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(username=username)
            user.check_password(password)
        except:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)
