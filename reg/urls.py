from django.urls import path

from reg.views import UserRegister, UserLogin

urlpatterns = [
    path('reg/', UserRegister.as_view(), name='user-reg'),
    path('login/', UserLogin.as_view(), name='user-log'),

]
