from django.urls import path
from .views import AdminObtainTokenView

urlpatterns = [
    path('login/', AdminObtainTokenView.as_view(), name='admin-obtain-token'),
]
