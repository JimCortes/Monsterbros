from rest_framework import serializers
from customer.serializers import CustomerSerializer  
from .models import Branch, Truck, Appointment, Notes
from customer.models import Customer


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Notes
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    truck = serializers.StringRelatedField(allow_null=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    notes = serializers.SerializerMethodField()

    
    class Meta:
        model = Appointment
        fields = '__all__'
        
    def get_customer_data(self, obj):
        customer = obj.customer
        return {
            'name': customer.name,
            'email': customer.email,
            'unit':customer.unit,
            'address':customer.address_line_1,
            'phone':customer.phone_number,
            'last_name':customer.last_name

        }
    def get_notes(self, instance):
        # Call the get_notes method of the Appointment model
        notes_queryset = instance.get_notes()
        notes_data = [{'user': note.user, 'notes': note.notes} for note in notes_queryset]
        return notes_data