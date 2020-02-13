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
    first_name = ''
    last_name = ''

    def get(self, request):
        self.first_name = request.data.get("first_name")
        self.last_name = request.data.get("last_name")
        usernames = [self.first_name.lower() + str(random.randrange(1, 100)) + self.last_name.lower(),
                     self.last_name.lower() + str(random.randrange(1, 100)) + self.first_name.lower(),
                     self.last_name.lower() + str(random.randrange(1, 100)),
                     self.first_name.lower() +str(random.randrange(1, 100)),
                     self.first_name[:3].lower()+ str(random.randrange(1, 100)) + self.last_name[:3].lower(),
                     self.last_name[:3].lower() + str(random.randrange(1, 100)) + self.first_name[:3].lower()
                     ]
        return Response({'usernames': usernames}, status=HTTP_200_OK)

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        phone_number = request.data.get("phone_number")

        if CustomUser.objects.filter(username=username).count() > 0:
            return Response({'error': 'This username is already exists'}, status=HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create(first_name=self.first_name, last_name=self.last_name, username=username,
                                         password=password, email=email)
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
