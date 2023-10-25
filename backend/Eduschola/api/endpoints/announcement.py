from api.serializers import AnnouncementSerializer
from Eduschola.models import Announcement
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

class CreateAnnouncementApiView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class ListAnnouncementApiView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
                       
        return Response({
            'message': 'Announcment deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
    
    