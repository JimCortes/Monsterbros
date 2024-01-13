from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from customer.models import Customer



class Branch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    branch_id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
   
    def __str__(self):
        return f"{self.name} - {self.owner}"


class Truck(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    truck_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    def get_notes(self):
        return Notes.objects.filter(appoiment_id=self.id)


    def __str__(self):
        return f"Appointment #{self.id} - Customer: {self.customer.name} - Branch: {self.branch.name} - Truck: {self.truck.name if self.truck else 'unassigned'} - Status: {self.status} - Time: {self.appointment_time}"

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    appoiment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    notes = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return  {self.id , self.note} 

