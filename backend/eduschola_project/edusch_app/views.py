from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import UserSerializer, StudentSerializer, ParentSerializer, InstructorSerializer, SchoolSerializer
from .models import User, Student, Instructor, Parent, School


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


class CreateSchoolApiView(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = SchoolSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        except ValidationError as error:
            return Response({'error': error.detail}, status=HTTP_400_BAD_REQUEST)
