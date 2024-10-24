from django.db import models
import base64
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest
from rest_framework.request import Request

from typing import Optional



from django.conf import settings
import os
import pycountry

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        
        """Create and return a user with an email and password."""
        
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_staff_user(self, email, password=None, **extra_fields):
        """Create and return a staff user with an email and password."""
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser'):
            raise ValueError('Staff users cannot be superusers.')
        
        return self.create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class AppUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    email_last_verified_at = models.DateTimeField(blank=True, null=True, default=None)
    email = models.EmailField(unique=True)
    mobile_phone_number = mobile_phone_number = models.CharField(max_length=64, null=True, blank=True)
    is_superuser = models.BooleanField(default=False,
                                       help_text=('Designates that this user has all '
                                                  'permissions without explicitly assigning them.'),
                                       verbose_name='superuser status')
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        app_label = 'core'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']
    
    
    objects = AppUserManager()
    
    @property
    def managed_restaurants(self):
        excluded_clients_ids = UserToRestaurant.objects.filter(user=self).values_list(
            'restaurant__id', flat=True,
        )
        return self.restaurants.exclude(id__in=excluded_clients_ids).order_by('usertorestaurant')

    


    def get_active_restaurant(self, request) -> Optional['Restaurant']:
        if request:
            if not self.is_staff:
                return None
            if request.user.is_anonymous or not request.user.is_staff:
                # method is called from an admin user for a regular user, or by anonymous user,
                # we do not have active client information here
                return None

            active_restaurant_id = None
            # attempt to retrieve active client based on request parameters
            if isinstance(request, Request):
                active_restaurant_id = request.query_params.get('active_restaurant')
            elif isinstance(request, HttpRequest):
                active_restaurant_id = request.GET.get('active_restaurant')

            if active_restaurant_id:
                active_restaurant = self.managed_restaurants.filter(id=active_restaurant_id).first()
                if active_restaurant:
                    if active_restaurant_id != request.session.get('active_restaurant_id'):
                        # save active client id in session if not already present
                        request.session['active_restaurant_id'] = active_restaurant_id
                        # reset permission cache since client might have changed
                        # active_client_changed.send(sender=self.__class__, user=self)
                    return active_restaurant

            active_restaurant_id = request.session.get('active_restaurant_id')
            active_restaurant = self.managed_restaurants.filter(id=active_restaurant_id).first()
            if active_restaurant:
                return active_restaurant
            # LOG.info('Active client not found from request, returning first client for user {}'.format(self.display))
        else:
            pass
            # LOG.warning('No request provided, returning first client for user {}'.format(self.display))
        active_restaurant = self.managed_restaurants.first()
        if request and active_restaurant:
            request.session['active_restaurant_id'] = active_restaurant.id
        return active_restaurant

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return None

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name


class CurrencyManager(models.Manager):
    def get_default_or_first(self):
        return self.filter(is_default=True).first() or self.first()
    

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=127)
    country = models.CharField(max_length=2, db_index=True, choices=[(country.alpha_2, country.name)
                                             for country in pycountry.countries])
    state = models.CharField(max_length=127, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=64)
    fax = models.CharField(max_length=64, blank=True, null=True)
    date_created = models.DateTimeField(db_index=True, auto_now_add=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='restaurants', through='UserToRestaurant')

    class Meta:
        app_label = 'core'
        ordering = ['-date_created']
        
    def get_default_currency(self):
        try:
            return self.currencies.filter(is_default=True).first()
        except (Currency.MultipleObjectsReturned, Currency.DoesNotExist):
            return None
        
        
        
        
class Currency(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="currencies")
    code = models.CharField(max_length=3,
                            choices=[(i.alpha_3, i.alpha_3) for i in pycountry.currencies])
    rate = models.DecimalField(default=1, max_digits=12, decimal_places=6)
    is_default = models.BooleanField(default=False)

    objects = CurrencyManager()

    class Meta:
        verbose_name_plural = 'currencies'
        app_label = 'core'

    def to_dict(self):
        return dict(code=self.code, rate=self.rate, is_default=self.is_default)

    def save(self, *args, **kwargs):
        if self.is_default:
            # NOTE(tomo): Remove any other defaults
            Currency.objects.filter(is_default=True).exclude(code=self.code).update(is_default=False)
        return super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.code
    
    
            
class UserToRestaurant(models.Model):
    """
    Map user accounts to Restaurant objects and store permissions

    Also stores (email) communications and notifications settings.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # roles = models.ManyToManyField('accounts.Role', related_name='users', blank=True)
    # invitation = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'restaurant')
        app_label = 'core'

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