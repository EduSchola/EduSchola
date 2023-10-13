from rest_framework import serializers

from django.contrib.auth.models import Group
from Eduschola.models import Assignment, Student, Parent, Staff, User, School, Grade, Course

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['username', 'password', 'role', 'school', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_id', 'name', 'address', 'contact_information']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class ParentUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer

    class Meta:
        model = Parent
        fields = ['parent_id', 'user', 'phone', 'email', 'address']


class ParentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Parent
        fields = ['parent_id', 'user', 'phone', 'email', 'address']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    parent = ParentSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['student_id', 'user', 'date_of_birth', 'phone_number', 'address', 'parent', 'school']


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = ['staff_id', 'user', 'phone', 'email', 'address', 'school', 'subjects', 'staff_role']

class GradeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = '__all__'
