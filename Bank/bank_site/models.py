from django.db import models

# Create your models here.
class customers(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    address = models.TextField()
    balance = models.FloatField()

class Transfer(models.Model):
    name = models.ForeignKey(customers,on_delete=models.CASCADE)
    revicer = models.CharField(max_length=255)
    send = models.FloatField()
