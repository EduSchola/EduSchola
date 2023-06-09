from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from api import create_announcement
from models import Announcement


class TestAnnouncement(TestCase):
    def test_create_announcement_with_all_required_parameters(self):
        announcement = Announcement()
        announcement.title = "Testing Announcement"
        announcement.body = "This's a test announcement."
        announcement.course_id = 1
        announcement.user_id = 1

        announcement.save()

        self.assertEqual(announcement.title, "Test Announcement")
        self.assertEqual(announcement.body, "This is a test announcement.")
        self.assertEqual(announcement.course_id, 1)
        self.assertEqual(announcement.user_id, 1)

    def test_create_announcement_with_invalid_parameters(self):
        with self.assertRaises(ValueError):
            announcement = Announcement()
            announcement.title = ""
            announcement.body = "This is a test announcement."
            announcement.course_id = 1
            announcement.user_id = 1

            announcement.save()

    def test_create_announcement_that_is_associated_with_a_course(self):
        announcement = Announcement()
        announcement.title = "Test Announcement"
        announcement.body = "This is a test announcement."
        announcement.course_id = 1
        announcement.user_id = 1

        announcement.save()

        self.assertEqual(announcement.course_id, 1)

    def test_create_announcement_that_is_associated_with_a_user(self):
        announcement = Announcement()
        announcement.title = "Test Announcement"
        announcement.body = "This is a test announcement."
        announcement.course_id = None
        announcement.user_id = 1

        announcement.save()

        self.assertEqual(announcement.user_id, 1)
