from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d',blank=True)


    def __str__(self):
        return f'Profile for user {self.user.username}'





class Booking(models.Model):
   
   
    def generate_random_id():
       return get_random_string(10,allowed_chars='0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

   
   
    order_id= models.CharField(default = generate_random_id(),max_length = 6,primary_key=True,unique= True)
    name=models.CharField(max_length=90)
    email=models.EmailField(max_length=111)
    to_address=models.CharField(max_length=111)
    from_address=models.CharField(max_length=111)
    phone =  models.CharField(max_length=15)
    weight = models.CharField(max_length=7)
    price = models.CharField(max_length=10)
    pickupdate= models.CharField(max_length=500)

    def __str__(self):
        return ( str(self.order_id) + self.name) 

   