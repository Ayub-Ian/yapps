from .models import QRCode, Restaurant, Currency, UserToRestaurant
from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('code', 'rate', 'is_default')

class QRCodeSerializer(serializers.ModelSerializer):
    image_base64 = serializers.CharField(read_only=True)

    class Meta:
        model = QRCode
        fields = [
            'id',
            'title',
            'table_number',
            'branch',
            'status',
            'creation_date',
            'expiry_date',
            'url',
            'image_base64'  
        ]
        
class RestaurantSerializer(serializers.ModelSerializer):
    currencies = CurrencySerializer(many=True)
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    
    class Meta:
        model = Restaurant
        fields = '__all__'
        
    def create(self, validated_data):
        currencies_data = validated_data.pop('currencies', [])
        users_data = validated_data.pop('users', [])
        
        restaurant = Restaurant.objects.create(**validated_data)

        for currency_data in currencies_data:
            Currency.objects.create(restaurant=restaurant, **currency_data)

        for user in users_data:
            UserToRestaurant.objects.create(user=user, restaurant=restaurant)

        return restaurant
    
# class RestaurantBriefSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restaurant
#         fields = (
#             'id', 'name', 'first_name', 'last_name', 'company', 'city', 'country', 'state', 'date_created', 'currency',
#             'phone', 'country_name', 'long_name', 'vat_id', 'status', 'address1', 'zip_code', 'roles', 'display',
#             'enough_credit',
#         )
#         read_only_fields = (
#             'id', 'name', 'country_name', 'long_name', 'currency', 'status', 'display', 'enough_credit',
#         )