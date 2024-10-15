from .models import QRCode
from rest_framework import serializers

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