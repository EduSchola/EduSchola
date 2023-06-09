
from django.test import TestCase
from .models import Assignment, Course
from django.utils import timezone

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
