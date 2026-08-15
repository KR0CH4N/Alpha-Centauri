from django.db import models
from planetclass.models import PlanetClass
from accounts.models import Account

# Create your models here.
class PlanetDiscovery(models.Model):
    id = models.AutoField(primary_key=True)
    planet_class_id = models.ForeignKey(PlanetClass, on_delete = models.CASCADE, null = True)
    account_id = models.ForeignKey(Account, on_delete = models.CASCADE, null = True)
    planet_name = models.CharField(max_length = 100)
    galaxy = models.CharField(max_length = 100)
    star_system = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    discovery_date = models.DateTimeField(auto_now = True)
    cover_image = models.CharField(max_length = 100, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
