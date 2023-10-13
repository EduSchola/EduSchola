from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.serializers import CourseSerializer
from Eduschola.models import Course

# create course:
class CreateCourseApiView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# list all courses:
class ListAllCourseApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# get, update or delete a single course
class DetailUpdateDeleteCourseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # lookup_field is the field that is used to retrieve the object
    lookup_field = 'pk'
