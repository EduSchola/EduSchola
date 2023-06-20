
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
import datetime
from .models import Assignment, Course, School
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse

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



# Create your tests here.

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
