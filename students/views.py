from rest_framework import views, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Student
from .serializers import StudentObtainTokenSerializer, StudentSerializer
from auth.authentication import Authentication


class StudentObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        student = Student.objects.filter(email=student_email, password=password).first()

        if student is None:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        jwt_token = Authentication.create_jwt_student(student)

        return Response({'token': jwt_token})




