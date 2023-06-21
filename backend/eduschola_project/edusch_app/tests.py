from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


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
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
