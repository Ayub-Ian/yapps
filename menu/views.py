from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response


from menu.models import Menu, MenuItem, Category
from menu.serializers import MenuSerializer, CategorySerializer
from core.models import Restaurant

# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        return Menu.objects.filter(restaurant_id=restaurant_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
class CategoryDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MenuDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Get the first category and its items
        first_category = instance.categories.first()
        if first_category:
            first_category_data = CategorySerializer(first_category).data
            return Response({
                'menu': serializer.data,
                'first_category': first_category_data
            })
        return Response({'menu': serializer.data, 'first_category': None})
