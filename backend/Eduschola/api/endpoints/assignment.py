from api.serializers import AssignmentSerializer
from Eduschola.models import Assignment
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

class CreateAssignmentApiView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ListAssignmentApiView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = 'pk'    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
                       
        return Response({
            'message': 'Assignment deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
    
    