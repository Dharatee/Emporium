from django.db import models
#from django.utils.timezone.now

# Create your models here.

class first(models.Model):
      name = models.CharField(max_length = 30)
      address = models.CharField(max_length = 20)
      submission = models.DateField("submitted date" #, default = timezone.now()
      )

 #def__str__(self):
   # return self.name

