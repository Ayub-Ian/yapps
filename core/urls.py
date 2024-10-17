from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QRCodeViewSet
from core.authentication.views import CustomTokenPairView, StaffRegisterView

from rest_framework_simplejwt.views import TokenRefreshView



router = DefaultRouter()
router.register(r'qrcode', QRCodeViewSet, basename='qrcode')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', StaffRegisterView.as_view(), name="auth_register"),
    path('login/', CustomTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
