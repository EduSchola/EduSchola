from rest_framework import serializers

from django.contrib.auth.models import Group
from Eduschola.models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'