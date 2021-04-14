from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    contactno = models.CharField(max_length=10)
