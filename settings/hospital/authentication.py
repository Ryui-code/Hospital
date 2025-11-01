from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

class CookieTokenAuthentication(BaseAuthentication): # Сохранить данные с регистрации пользователя для последующих запросов пользователя
    def authenticate(self, request):
        token = request.COOKIES.get('auth_token') # Получить токен с созданных пользователей (auth_token)
        if not token:
            return None

        try:
            user = CustomUser.objects.get(token=token)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return user, None # Возвращать если есть пользователь с таким токеном, если нет ничего не возвращать