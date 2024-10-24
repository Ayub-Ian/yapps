
import qrcode
import os
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.decorators import throttle_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsSuperUserOrReadOnly
from .models import QRCode, Restaurant
from .serializers import QRCodeSerializer, RestaurantSerializer

def generate_qr_code(qr_code_data, qr_code_id):
    """Generate a QR code image and save it to the media directory."""
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in the QR code grid
        border=4,  # thickness of the border (minimum is 4)
    )
    
    # Add data to the QR Code
    qr.add_data(qr_code_data)
    qr.make(fit=True)  # Fit the QR Code to the data

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Define the file path to save the QR code image
    qr_image_path = os.path.join(settings.MEDIA_ROOT, f"{qr_code_id}.png")

    # Save the QR Code image
    img.save(qr_image_path)

    return qr_image_path  # Optionally return the path

class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

    def perform_create(self, serializer):
        
        qr_code_instance = serializer.save()

        qr_data = qr_code_instance.url #The URL that will be redirected
      
        # Save QR code image
        qr_image_path = generate_qr_code(qr_data, qr_code_instance.id)
       
        # qr_code_instance.save(update_fields=['url'])
        
class RestaurantViewSet(viewsets.ModelViewSet):
    
    
    serializer_class = RestaurantSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    
    
    def get_queryset(self):
        return Restaurant.objects.all()
    


@api_view(['GET'])
@permission_classes([AllowAny])
def current_user(request):
    if request.user.is_authenticated and request.user.is_staff:
        response_data = {
            'user': get_current_user_info(request)
        }
        return Response(response_data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)
        



def get_current_user_info(request):
    user = request.user
    restaurants = RestaurantSerializer(user.managed_restaurants.all(), many=True)
    active_restaurant = user.get_active_restaurant(request=request)


    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'full_name': user.get_full_name(),
        'email': user.email,
        'restaurants': restaurants.data,
        'active_restaurant': active_restaurant.id if active_restaurant else None,

    }