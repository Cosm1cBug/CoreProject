from apps.user.models import CustomUser
from ninja.security import HttpBearer
from .models import Token
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest


class AuthBearer(HttpBearer):
    def authenticate(
        self,
        request: HttpRequest,
        token: str,
    ) -> CustomUser | AnonymousUser:
        try:
            token_data = Token.objects.get(token=token)
            return token_data.user

        except Token.DoesNotExist:
            return AnonymousUser