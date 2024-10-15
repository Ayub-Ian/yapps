from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QRCodeViewSet

router = DefaultRouter()
router.register(r'qrcode', QRCodeViewSet, basename='qrcode')

urlpatterns = [
    path('', include(router.urls)),
]
