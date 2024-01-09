from rest_framework import serializers
from customer.serializers import CustomerSerializer  
from .models import Branch, Truck, Appointment
from customer.models import Customer


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    truck = serializers.StringRelatedField(allow_null=True)
    customer = serializers.StringRelatedField()


    class Meta:
        model = Appointment
        fields = '__all__'