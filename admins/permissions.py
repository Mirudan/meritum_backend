import jwt
from rest_framework.exceptions import AuthenticationFailed, ParseError
from rest_framework.permissions import BasePermission
from auth.authentication import Authentication
from meritum import settings


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None
        jwt_token = Authentication.get_the_token_from_header(jwt_token)
        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()
        return payload['role'] == 'admin'