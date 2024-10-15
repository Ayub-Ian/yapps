from django.db import models
import base64
from django.core.files.base import ContentFile

from django.conf import settings
import os

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    # Other restaurant fields...

class QRCode(models.Model):
    title = models.CharField(max_length=50)
    table_number = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Expired', 'Expired')], default='Active')
    creation_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "QR Code"
        verbose_name_plural = "QR Codes"
        app_label = 'core'
        
    @property
    def image_base64(self):
        """Return the QR code image as a Base64 string."""
        image_path = os.path.join(settings.MEDIA_ROOT, f"{self.id}.png")
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the original save method
        self.url = self.generate_qr_code_url()  # Generate the QR code URL
        super().save(update_fields=['url'])  # Save the updated QR code URL

    def generate_qr_code_url(self):
        """Construct the redirect URL for the QR code."""
        return "http://localhost:3000/ke/roast-grill/menu/1"
                
    def __str__(self):
        return self.title