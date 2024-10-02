
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu.views import MenuViewSet, MenuDetailViewSet, CategoryDetailViewSet

router = DefaultRouter()
router.register(r'restaurants/(?P<restaurant_id>\d+)/menus', MenuViewSet, basename='menu')
router.register(r'menus', MenuDetailViewSet, basename='menu-detail')
router.register(r'categories', CategoryDetailViewSet, basename='category-detail')



urlpatterns = [
    path('', include(router.urls)),
]
