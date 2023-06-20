
from django.test import TestCase
from .models import Assignment, Course
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

from eduschola_project.edusch_app.models import School


# Create your tests here.

class CreateSchoolAPITestCase(TestCase):

    def test_that_school_is_created(self):
        url = reverse('create-school')
        data = {
            'name': 'British international school',
            'address': 'Lekki',
            'contact_information': "09081167465"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_for_missing_fields(self):
        url = reverse('create-school')
        data = {
            'name': 'British international school',
            'address': 'Lekki',
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

