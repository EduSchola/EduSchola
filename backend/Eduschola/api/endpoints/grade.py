from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.serializers import GradeSerializer, UserSerializer
from Eduschola.models import Grade


class GradeView(generics.CreateAPIView, 
                generics.ListAPIView):

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


    def create(self, request, *args, **kwargs):
        try:
            grade_data = request.data
            serilaizer = self.get_serializer(data=grade_data)

            if serilaizer.is_valid(raise_exception=True):
                serilaizer.save()

                return Response ({
                    'success':True,
                    'data': serilaizer.data
                }, status= status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     if not queryset.exisits():
    #         return Response({
    #             'success':False,
    #             'message':'Grade does not exisit'
    #         }, status=status.HTTP_404_NOT_FOUND)

    #     grade_serializer = self.get_serializer(queryset, many=True)

    #     return Response({
    #         'success': True,
    #         'data': grade_serializer.data
    #     }, statuss=status.HTTP_200_OK)
        
class GradeDeleteUpdateRetrieveView(generics.DestryoAPIView,
                                    generics.UpdateAPIView,
                                    generics.RetrieveAPIView):
    
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field =' pk'

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response({
                'success': True,
                'message': 'Grade deleted successfully.'
            }, status=status.HTTP_204_NO_CONTENT)

        except Grade.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Grade not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Grade does not exist.'
            }, status=status.HTTP_404_NOT_FOUND)

        # Extract the 'gradeScore' field from the request data
        grade_score = request.data.get('gradeScore')

        if grade_score is not None:
            # Update the 'gradeScore' field of the instance
            instance.gradeScore = grade_score
            instance.save()

            return Response({
                'success': True,
                'message': 'Grade score updated successfully.',
                'data': GradeSerializer(instance).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'message': 'Missing or invalid data for gradeScore.'
            }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Grade does not exist.'
            }, status=status.HTTP_404_NOT_FOUND)

        grade_serializer = self.get_serializer(instance)

        return Response({
            'success': True,
            'data': grade_serializer.data
        }, status=status.HTTP_200_OK)