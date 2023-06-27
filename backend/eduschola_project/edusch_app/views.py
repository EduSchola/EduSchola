from uuid import UUID

from django.db.models import IntegerField, BigIntegerField
from django.db.models.functions import Cast
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, StudentSerializer, ParentSerializer, InstructorSerializer, CourseSerializer
from .models import User, Student, Instructor, Parent, Course
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import UserSerializer, StudentSerializer, ParentSerializer, InstructorSerializer, SchoolSerializer, AssignmentSerializer
from .models import User, Student, Instructor, Parent, School, Assignment



# Create your views here.

# Student View
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def createStudent(self, request, *args, **kwargs):
        # Extract the user data from the request data
        user_data = request.data.pop('user', {})

        # Create a new user instance using the user data
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Add the created user instance to the student data
        request.data['user'] = user.id

        # Create the student instance
        return super().create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def updateStudent(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Extract the user data from the request data
        user_data = request.data.pop('user', {})

        # Retrieve the existing user instance associated with the student
        user = instance.user

        # Update the existing user instance with the new data
        user_serializer = UserSerializer(user, data=user_data, partial=partial)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Add the updated user instance ID to the student data
        request.data['user'] = user.id

        # Update the student instance
        return super().update(request, *args, **kwargs)


# Parent Views
class ParentListCreateView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def createParent(self, request, *args, **kwargs):
        # Extract the user data from the request data
        user_data = request.data.pop('user', {})

        # Create a new user instance using the user data
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Add the created user instance to the student data
        request.data['user'] = user.id

        # Create the student instance
        return super().create(request, *args, **kwargs)


class ParentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def updateParent(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Extract the user data from the request data
        user_data = request.data.pop('user', {})

        # Retrieve the existing user instance associated with the student
        user = instance.user

        # Update the existing user instance with the new data
        user_serializer = UserSerializer(user, data=user_data, partial=partial)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Add the updated user instance ID to the student data
        request.data['user'] = user.id

        # Update the student instance
        return super().update(request, *args, **kwargs)


class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def createInstructor(self, request, *args, **kwargs):
        # Extract the user data from the request data
        user_data = request.data.pop('user', {})

        # Create a new user instance using the user data
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Add the created user instance to the student data
        request.data['user'] = user.id

        # Create the student instance
        return super().create(request, *args, **kwargs)


class InstructorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def updateInstructor(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Extract the user data from the request data
        user_data = request.data.pop('user', {})

        # Retrieve the existing user instance associated with the student
        user = instance.user

        # Update the existing user instance with the new data
        user_serializer = UserSerializer(user, data=user_data, partial=partial)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Add the updated user instance ID to the student data
        request.data['user'] = user.id

        # Update the student instance
        return super().update(request, *args, **kwargs)



# create or get all  course
@api_view(['POST', 'GET'])
def create_or_list_all_courses(request):
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# get, update or delete a single course
@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_courseDetail(request, pk):
    # get course based on pk:
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreateAssignmentApiView(generics.CreateAPIView):
    serializer_class = AssignmentSerializer


class AssignmentApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = 'id'  #lookup_field is the field that is used to retrieve the object

class ListAssignmentApiView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class CreateSchoolApiView(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()



