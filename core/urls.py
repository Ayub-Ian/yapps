from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QRCodeViewSet, RestaurantViewSet, current_user
from core.authentication.views import StaffRegisterView

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView



router = DefaultRouter()
router.register(r'qrcodes', QRCodeViewSet, basename='qrcode')
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', StaffRegisterView.as_view(), name="auth_register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current-user', current_user, name="current-user" )
]
