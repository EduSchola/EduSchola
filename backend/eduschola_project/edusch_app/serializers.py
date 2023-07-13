from rest_framework import serializers

from django.contrib.auth.models import Group
from .models import Student, Parent, Staff, User, School, Grade, Assignment, Course


class UserSerializer(serializers.ModelSerializer):
    # groups = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User

        fields = ['username', 'password', 'role', 'school', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_id', 'name', 'address', 'contact_information']


class ParentUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer

    class Meta:
        model = Parent
        fields = ['parent_id', 'user', 'tel', 'email', 'address']


class ParentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Parent
        fields = ['parent_id', 'user', 'tel', 'email', 'address']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    parent = ParentSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['student_id', 'user', 'date_of_birth', 'phone_number', 'address', 'parent', 'school']


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    # school = SchoolSerializer(read_only=True)
    class Meta:
        model = Staff
        fields = ['staff_id', 'user', 'phone', 'email', 'address', 'school', 'subjects', 'staff_role']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
