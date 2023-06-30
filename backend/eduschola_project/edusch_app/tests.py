
import unittest
from django.urls import reverse

from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse
import datetime
from .models import Assignment, Course, School, Student, Parent, Staff
from django.utils import timezone
from rest_framework import status
from .serializers import StudentSerializer
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

class AssignmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Course.objects.create(name='Test Course', description='Description')
        Assignment.objects.create(title='Test Assignment', description='Description', issue_date=timezone.now(), due_date=timezone.now() + timezone.timedelta(days=7), course=Course.objects.get(id=1))

    def test_issue_date_not_in_past(self):
        assignment = Assignment.objects.get(id=1)
        self.assertTrue(assignment.issue_date >= timezone.now())

    def test_due_date_after_issue_date(self):
        assignment = Assignment.objects.get(id=1)
        self.assertTrue(assignment.due_date > assignment.issue_date)




    def test_create_student_success(self):
        response = self.client.post(self.student_url, self.valid_student_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_OK)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().user.username, 'student81')

    def test_create_student_failure(self):
        # Simulate a failed request by removing required fields from the payload
        invalid_payload = self.valid_student_payload.copy()
        invalid_payload.pop('user')
        response = self.client.post(self.student_url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Student.objects.count(), 0)
    
       
class CreateSchoolAPITestCase(TestCase):

    def test_that_school_is_created(self):
        url = reverse('create-school')
        data = {
            'name': '',
            'address': '',
            'contact_information': ""
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_for_missing_fields(self):
        url = reverse('create-school')
        data = {
            'name': '',
            'address': '',
        }

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


class AssignmentTests(APITestCase):
    
    def setUp(self): # this method runs before each test
        self.assignment1 = Assignment.objects.create(
            title='Test Assignment 1',
            description='This is a test assignment',
            issue_date=timezone.now(),
            due_date=timezone.now() + datetime.timedelta(days=7),
        )
        
        self.assignment2 = Assignment.objects.create(
            title='Test Assignment 2',
            description='This is another test assignment',
            issue_date=timezone.now(),
            due_date=timezone.now() + datetime.timedelta(days=7),
        )

    def test_create_assignment(self):
        
        #Ensure we can create a new assignment.
        
        url = reverse('assignment-list')   
        data = {
            'title': 'Test Assignment',
            'description': 'This is a test assignment',
            'issue_date': timezone.now(),
            'due_date': timezone.now() + datetime.timedelta(days=7),
            # add other necessary fields
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Assignment.objects.count(), 2)
        self.assertEqual(Assignment.objects.get(title='Test Assignment').description, 'This is a test assignment')

    def test_retrieve_assignment(self):
        """
        Ensure we can retrieve an assignment.
        """
        url = reverse('assignment-retrieve-update-delete', kwargs={'pk': self.assignment1.pk})  # replace with your URL name
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.assignment1.title)

    def test_update_assignment(self):
        """
        Ensure we can update an assignment.
        """
        url = reverse('assignment-retrieve-update-delete', kwargs={'pk': self.assignment1.pk})  # replace with your URL name
        data = {
            'title': 'Updated Assignment',
            'description': 'This is an updated test assignment',
            # add other necessary fields
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Assignment.objects.get(pk=self.assignment1.pk).title, 'Updated Assignment')

    def test_delete_assignment(self):
        """
        Ensure we can delete an assignment.
        """
        url = reverse('assignment-retrieve-update-delete', kwargs={'pk': self.assignment1.pk})  # replace with your URL name
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Assignment.objects.count(), 1)

