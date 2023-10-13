from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from api.serializers import SchoolSerializer
from Eduschola.models import School

class CreateSchoolApiView(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()