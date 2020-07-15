import random

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from reg.models import CustomUser, SecurityNumber
from django.core.mail import send_mail
import re

REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check_mail(email):
    # pass the regular expression
    # and the string in search() method
    if (re.search(REGEX, email)):
        return True

    else:
        return False


class UserRegisterConfirmEmail(APIView):

    def post(self, request):
        email = request.data.get("email")
        if check_mail(email):
            confirmation_number = (random.randint(100000, 999999))
            send_mail('GenLib', 'Security number:{}'.format(confirmation_number),
                      'izzattilla706@gmail.com', [email], fail_silently=False)
            SecurityNumber.objects.create(secure_number=confirmation_number, email=email)
            return Response({'status': True,
                             'email': email})
        else:
            return Response({'status': 'Email not Valid'})


class UserRegisterCheckNumber(APIView):
    def post(self, request):
        security_number = request.data.get('security_number')
        try:
            secure_number = SecurityNumber.objects.get(secure_number=security_number)
        except SecurityNumber.DoesNotExist:
            secure_number = None
        if secure_number is not None:
            secure_number.delete()
            return Response({'Confirmed': True})
        else:
            return Response({'Confimed': False})


class UserRegister(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        password = request.data.get("password")
        user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        token = Token.objects.create(user=user)
        return Response({'username': user.username,
                         'password': user.password,
                         'token': token.key}, status=HTTP_200_OK, )


class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(email=email)
            user.check_password(password)
        except:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)
