from rest_framework import serializers
from menu.models import MenuItem, Menu

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, required=False)

    class Meta:
        model = Menu
        fields = '__all__'
