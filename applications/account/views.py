from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from applications.account.serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистровались. Вам отправлено письмо на почту с активацией', status=201)


class ActivationAPIView(APIView):
    def get(self, request, activation_code):
        # try:
        #     user = User.objects.get(activation_code=activation_code)
        # except User.DoesNotExist:
        #     return Response('Неправильной код активации', status=400)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_active', 'activation_code'])
        return Response('Успешно', status=200)
    

# class LoginAPIView(ObtainAuthToken):
#     serializer_class = LoginSerializer
    

# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request): # разлогин дз
#         user = get_object_or_404(Token, user=request.user)
#         user.delete()
#         # request.user.auth_token.delete()
        
#         return Response('Пользователь успешно вышел из системы')


# class ChangePasswordAPIView(APIView):
#     def post(self, request): # смена пароля
#         ...    
        

   
# TODO: реализовать ForgotPassword

