# Create your models here.
from django.db import models

class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20)
    unit = models.CharField(max_length=10, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.last_name}"
