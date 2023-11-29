from django.test import TestCase

# myapp/tests/test_models.py
from django.test import TestCase
from .models import Customer


class CustomerModelTest(TestCase):
    def setUp(self):
        # Create a sample customer for testing
        self.customer = Customer.objects.create(
            name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='1234567890',
            zip_code='12345',
            unit='A101',
            address_line_1='123 Main St',
            state='CA',
            city='Cityville',
            origin='Web'
        )

    def test_customer_str_representation(self):
        # Test the __str__ method of the Customer model
        self.assertEqual(str(self.customer), 'John Doe')

    def test_customer_email_unique_constraint(self):
        # Test the unique constraint on the email field
        duplicate_customer = Customer(
            name='Jane',
            last_name='Doe',
            email='john.doe@example.com',  # Duplicate email
            phone_number='9876543210',
            zip_code='54321',
            address_line_1='456 Oak St',
            state='NY',
            city='Townsville',
            origin='Mobile'
        )

        with self.assertRaises(Exception):
            # Attempt to save a duplicate email should raise an exception
            duplicate_customer.save()