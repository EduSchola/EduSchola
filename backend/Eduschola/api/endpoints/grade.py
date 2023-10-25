from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.serializers import GradeSerializer, UserSerializer
from Eduschola.models import Grade


class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
                       
        return Response({
            'message': 'Grade deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)