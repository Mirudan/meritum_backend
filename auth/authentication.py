from datetime import datetime, timedelta
import jwt
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError
from admins.models import Admin
from meritum import settings
from students.models import Student


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
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

        student = payload.get('student_id')
        if student is None:
            admin = payload.get('admin_id')
        if student is None and admin is None:
            raise AuthenticationFailed('User identifier not found in JWT')

        if student is not None:
            user = Student.objects.filter(student_id=student).first()
            if user is None:
                raise AuthenticationFailed('Student not found')
        else:
            user = Admin.objects.filter(admin_id=admin).first()
            if user is None:
                raise AuthenticationFailed('Admin not found')

        return user, payload

    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt_student(cls, student):
        payload = {
            'student_id': student.student_id,
            'exp': int((datetime.now() + timedelta(hours=settings.TOKEN_LIFETIME_HOURS)).timestamp()),
            'iat': datetime.now().timestamp(),
            'role': 'student',
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def create_jwt_admin(cls, admin):
        payload = {
            'admin_id': admin.admin_id,
            'exp': int((datetime.now() + timedelta(hours=settings.TOKEN_LIFETIME_HOURS)).timestamp()),
            'iat': datetime.now().timestamp(),
            'role': 'admin',
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')
        return token