from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.serializers import ParentSerializer, UserSerializer
from Eduschola.models import Parent

class ParentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = 'pk'

    # Modify parent details
    def patch(self, request, *args, **kwargs):
        parent = self.get_object()
        parent_serializer = self.get_serializer(instance=parent, data=request.data, partial=True)

        if parent_serializer.is_valid(raise_exception=True):
            parent_serializer.save()

            user_data = request.data.get('user')
            if user_data:
                user = parent.user
                user_serializer = UserSerializer(instance=user, data=user_data, partial=True)
                user_serializer.is_valid(raise_exception=True)
                user_serializer.save()

            return Response({
                'success': True,
                'data': parent_serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'data': parent_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Delete parent details
    def delete(self, request, *args, **kwargs):
        parent = self.get_object()
        parent.delete()

        return Response({
            'success': True,
            'message': 'Parent deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    # Retrieve Parent details by parent_id
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Parent not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class ParentCreateListView(generics.CreateAPIView, generics.ListAPIView):
    # Retrieve all parents details

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def create(self, request, *args, **kwargs):
        try:
            parent_data = request.data.copy()
            user_data = parent_data.pop('user')

            user_serializer= UserSerializer(data=user_data)
            parent_serializer = self.get_serializer(data=parent_data)

            user_serializer.is_valid(raise_exception=True)
            parent_serializer.is_valid(raise_exception=True)

            user = user_serializer.save()
            parent_data['user'] = user.user_id
            parent_serializer.save(user=user)

            return Response({
                'success': True,
                'data': parent_serializer.data                
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'success':False,
                'message': str(e)
            }, status = status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'success': True,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

