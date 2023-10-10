from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User
# Create your models here.

class FieldsModel(models.Model):
    field_name = models.CharField(max_length=100,default=' ')
    field_adress = models.CharField(max_length=200,default=' ')
    field_contact = models.CharField(max_length=150)
    field_image = models.ImageField(default=' ')
    field_size = models.CharField(max_length=100,default=' ')
    price_of_bron_per_minute = models.CharField(max_length=150)
    
    
    def __str__(self) -> str:
        return self.field_name


class BronModel(models.Model):
    day = models.DateField(default=date.today)
    start_time = models.DateTimeField(default=datetime.now) 
    end_time = models.DateTimeField(default=datetime.now) 
    field = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.day
    
