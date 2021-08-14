from django.db import models


# Create your models here.
class donatetable(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    type_of_donation = models.TextField()

class requesttable(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    type_of_donation = models.TextField()
