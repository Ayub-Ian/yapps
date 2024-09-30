from django.shortcuts import render

from rest_framework import viewsets

from menu.models import Menu, MenuItem
from menu.serializers import MenuSerializer

# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def perform_create(self, serializer):
        menu = serializer.save()
        items_data = self.request.data.get('items')
        if items_data:
            for item_data in items_data:
                MenuItem.objects.create(menu=menu, **item_data)

    def perform_update(self, serializer):
        menu = serializer.save()
        items_data = self.request.data.get('items')
        if items_data:
            menu.items.all().delete()  # Optionally delete existing items
            for item_data in items_data:
                MenuItem.objects.create(menu=menu, **item_data)
