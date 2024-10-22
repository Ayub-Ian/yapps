from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from core.models import AppUser


class StaffRegisterView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer