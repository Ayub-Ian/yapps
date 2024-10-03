from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    # Other restaurant fields...
