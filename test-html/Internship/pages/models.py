from django.db import models
from django.contrib.gis.db.models import PointField

# Create your models here.
class polygon(models.Model):
    notam = models.CharField(max_length=255)
    
    
    def __str__(self): 
        return self.notam