from rest_framework import serializers
from .models import Student, Parent, Instructor, User

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


