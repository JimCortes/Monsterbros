# viewsets.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Branch, Truck, Appointment, Notes
from customer.models import Customer
from .serializers import BranchSerializer, TruckSerializer, AppointmentSerializer, NotesSerializer
from customer.serializers import  CustomerSerializer
from datetime import datetime

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


    def list(self, request, *args, **kwargs):
        appointments = self.get_queryset()
        serialized_appointments = []

        for appointment in appointments:
            serialized_appointment = self.get_serializer(appointment).data
            serialized_appointment['customer_data'] = {
            'name': appointment.customer.name,
            'email': appointment.customer.email,
            'unit':appointment.customer.unit,
            'address':appointment.customer.address_line_1,
            'phone':appointment.customer.phone_number,
            'last_name': appointment.customer.last_name
            }
            serialized_appointments.append(serialized_appointment)

        return Response(serialized_appointments)


