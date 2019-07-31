from django.db import models

# Create your models here.
class registration(models.Model):
    First_Name = models.TextField(max_length=20, blank=False)
    Middle_Name = models.TextField(max_length=20)
    Last_Name = models.TextField(max_length=20, blank=False)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=25)
    Email = models.EmailField(primary_key = True, blank=False) #null=false by default
    Contact = models.BigIntegerField(max_length = 10, blank=False)


