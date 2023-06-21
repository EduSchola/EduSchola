import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student, Parent, Staff
from .serializers import StudentSerializer
from django.test import TestCase, Client
from .views import StudentView, ParentView, StaffView 

class EduScholaViewTestCase(TestCase):
    def setUp(self):
        self.student_url = reverse('student-list')
        self.valid_student_payload = {
            "user": {
                "username": "student81",
                "password": "password123",
                "role": "student",
                "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
                "first_name": "John",
                "last_name": "Doe"
            },
            "parent": {
                "user": {
                    "username": "parent81",
                    "password": "password456",
                    "role": "parent",
                    "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
                "tel": "1234567890",
                "email": "jane.smith@example.com",
                "address": "123 Street, City"
            },
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        }

        pass

    def test_create_student_success(self):
        response = self.client.post(self.student_url, self.valid_student_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().user.username, 'student81')

    def test_create_student_failure(self):
        # Simulate a failed request by removing required fields from the payload
        invalid_payload = self.valid_student_payload.copy()
        invalid_payload.pop('user')
        response = self.client.post(self.student_url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Student.objects.count(), 0)
    
        