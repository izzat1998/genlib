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
        email = request.data.get('email')
        password = request.data.get("password")
        phone_number = request.data.get("phone_number")

        if first_name is None or last_name is None:
            return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        if not username:
            username = str(first_name.lower) + str(last_name.lower)
        n = random.randint(100000, 999999)
        send_mail('Hello It is from GenLib',
                  f'This is activation code {n}',
                  'izzattilla706@gmail.com',
                  [f'{email}'],
                  fail_silently=False)
        user = CustomUser.objects.create(first_name=first_name, last_name=last_name, username=username,
                                         password=password, phone_number=phone_number)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id': user.user_id},

                        status=HTTP_200_OK)


class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(username=username, password=password)
        except:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)
