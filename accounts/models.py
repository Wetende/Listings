from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing

# Create your models here.
class UserProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def get_listings(self):
        return Listing.objects.order_by('-list_date').filter(user=self.user)