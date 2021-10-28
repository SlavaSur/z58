from django.db import models

# Create your models here.

class Product (models.Model):
    title = models.CharField(unique=True, max_length=10)
    diskription = models.TextField (max_length=300, null=True, blank=True)
    date_of_create = models.DateTimeField (auto_now_add=True, editable=False)