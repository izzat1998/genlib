from django.urls import path

from reg.views import UserRegister, UserLogin, UserRegisterConfirmEmail, UserRegisterCheckNumber

urlpatterns = [
    path('confirm_mail/', UserRegisterConfirmEmail.as_view(), name='user-confirm-mail'),
    path('check_code/', UserRegisterCheckNumber.as_view(), name='user-check-code'),
    path('reg/', UserRegister.as_view(), name='user-reg'),
    path('login/', UserLogin.as_view(), name='user-log'),

]
