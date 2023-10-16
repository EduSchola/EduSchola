from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.serializers import UserSerializer, StudentSerializer, ParentUserSerializer, ParentSerializer
from Eduschola.models import Student

class StudentView(
    generics.CreateAPIView,
    generics.ListAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        try:
            student_data = request.data.copy()
            user_data = student_data.pop('user')

            user_serializer= UserSerializer(data=user_data)
            student_serializer = self.get_serializer(data=student_data)

            user_serializer.is_valid(raise_exception=True)
            student_serializer.is_valid(raise_exception=True)

            user = user_serializer.save()
            student_data['user'] = user.user_id
            student_serializer.save(user=user)

            return Response({
                'success': True,
                'data': student_serializer.data                
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'success':False,
                'message': str(e)
            }, status = status.HTTP_400_BAD_REQUEST)
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            return Response({
                'success': False,
                'message': 'No students found.'
            }, status=status.HTTP_404_NOT_FOUND)

        student_serializer = self.get_serializer(queryset, many=True)

        return Response({
            'success': True,
            'data': student_serializer.data
        }, status=status.HTTP_200_OK)

    
    
class StudentRetrieveUpdateDestroyView(generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,):    

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Student not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        student_serializer = self.get_serializer(instance, data=request.data, partial=True)
        if student_serializer.is_valid(raise_exception=True):
            student_serializer.save()

            user_data = request.data.get('user')
            if user_data:
                user = instance.user
                user_serializer = UserSerializer(instance=user, data=user_data, partial=True)

                if user_serializer.is_valid(raise_exception=True):
                    user_serializer.save()

            return Response({
                'success': True,
                'data': student_serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'data': student_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Student not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        self.perform_destroy(instance)
        return Response({
            'success': True,
            'message': 'Student deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Student not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        student_serializer = self.get_serializer(instance)
        user_serializer = UserSerializer(instance=instance.user)

        return Response({
            'success': True,
            'data': {
                'student': student_serializer.data,
                'user': user_serializer.data
            }
        }, status=status.HTTP_200_OK)
    
