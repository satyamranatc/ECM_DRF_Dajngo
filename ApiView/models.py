from django.db import models

# Create your models here.
class Products(models.Model):
    PImage  = models.ImageField(upload_to="images/")
    Pname = models.CharField(max_length=200)
    Pdescription = models.TextField()
    Pprice = models.DecimalField(max_digits=10, decimal_places=2)