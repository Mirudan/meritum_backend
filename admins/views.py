from rest_framework import views, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Admin
from .serializers import AdminObtainTokenSerializer, AdminSerializer
from auth.authentication import Authentication


class AdminObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdminObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        admin_login = serializer.validated_data.get('login')
        password = serializer.validated_data.get('password')

        admin = Admin.objects.filter(login=admin_login, password=password).first()

        if admin is None:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        jwt_token = Authentication.create_jwt_admin(admin)

        return Response({'token': jwt_token})

