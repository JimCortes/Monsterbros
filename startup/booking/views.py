# viewsets.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Branch, Truck, Appointment
from .serializers import BranchSerializer, TruckSerializer, AppointmentSerializer
from customer.serializers import  CustomerSerializer
from datetime import datetime

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentsApiView(APIView):
    def get(self, request, year, month, day, customer_id):
        try:
            # Create a datetime object for the specified day
            target_date = datetime(year, month, day)

            # Retrieve appointments for the specified day
            appointments = Appointment.objects.filter(appointment_time__date=target_date)
            appointments_serializer = AppointmentSerializer(appointments, many=True)

            # Extract unique customer IDs from the appointments
            customer_ids = appointments.values_list('customer', flat=True).distinct()

            # Retrieve customer data for the unique customer IDs
            customers = Customer.objects.filter(customer_id__in=customer_ids)
            customers_serializer = CustomerSerializer(customers, many=True)

            # Combine customer and appointment data
            merged_data = {
                'customers': customers_serializer.data,
                'appointments': appointments_serializer.data
            }

            return Response(merged_data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)
