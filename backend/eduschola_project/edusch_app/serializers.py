from rest_framework import serializers
from .models import Student, Parent, Instructor, User, Course, School


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Parent
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):

        # Extract the related data object from the user_data sent:
        course_teacher = validated_data.pop('teacher', None)
        course_school = validated_data.pop('school', None)

        # Create a course object from the validated data sent:
        course = Course.objects.create(**validated_data)

        # Check if related data object then persist into course object:
        if course_teacher:
            teacher = Instructor.objects.create(course_teacher)
            course.teacher = teacher
            course.save()
        if course_school:
            school = School.objects.create(course_school)
            course.school = school
            course.save()
        return course


