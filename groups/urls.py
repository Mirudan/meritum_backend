from django.urls import path
from .views import SpecializationAPIList

urlpatterns = [
    path('', SpecializationAPIList.as_view(), name='специализации')
]