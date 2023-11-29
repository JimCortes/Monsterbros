from django.db import models
from django.contrib.auth.models import User



class Branch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} - {self.owner} - {self.country}, {self.state}, {self.city} - Created at: {self.created_at}"


class BranchAvailability(models.Model):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    daily_start_time = models.TimeField(null=True, blank=True)
    daily_end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.branch} - {self.is_available} ({self.daily_start_time} to {self.daily_end_time})"



class Truck(models.Model):
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, blank=True, null=True)
    customer_name = models.CharField(max_length=255)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        return f"{self.customer_name} - {self.appointment_time}"
