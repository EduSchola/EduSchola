from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from api.serializers import StaffSerializer, UserSerializer
from Eduschola.models import Staff

class StaffView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    # Create new staff
    def create(self, request, *args, **kwargs):
        try:
            staff_data = request.data.copy()
            user_data = staff_data.pop('user')

            user_serializer = UserSerializer(data=user_data)
            staff_serializer = self.get_serializer(data=staff_data)

            user_serializer.is_valid(raise_exception=True)
            staff_serializer.is_valid(raise_exception=True)

            user = user_serializer.save()
            staff_data['user'] = user.user_id
            staff_serializer.save(user=user)

            return Response({
                'success': True,
                'data': staff_serializer.data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve all staff details
    def list(self, request, *args, **kwargs):
        try:
            staff = Staff.objects.all()
            staff_serializer = self.get_serializer(instance=staff, many=True)

            return Response({
                'success': True,
                'data': staff_serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class StaffRetrieveView(generics.UpdateAPIView, generics.DestroyAPIView,
                generics.RetrieveAPIView,):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    lookup_field = 'pk'

    # Modify staff details
    def patch(self, request, *args, **kwargs):
        try:
            staff = self.get_object()
            staff_serializer = self.get_serializer(instance=staff, data=request.data, partial=True)

            staff_serializer.is_valid(raise_exception=True)
            staff_serializer.save()

            user_data = request.data.get('user')
            if user_data:
                user = staff.user
                user_serializer = UserSerializer(instance=user, data=user_data, partial=True)
                user_serializer.is_valid(raise_exception=True)
                user_serializer.save()

            return Response({
                'success': True,
                'data': staff_serializer.data
            }, status=status.HTTP_200_OK)

        except Staff.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Staff not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # Delete staff details and related user details
    def delete(self, request, *args, **kwargs):
        try:
            staff = self.get_object()
            staff.delete()

            return Response({
                'success': True,
                'message': 'Staff deleted successfully.'
            }, status=status.HTTP_204_NO_CONTENT)

        except Staff.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Staff not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve Staff details by staff_id
    def retrieve(self, request, *args, **kwargs):
        try:
            staff = self.get_object()
            staff_serializer = self.get_serializer(instance=staff)

            return Response({
                'success': True,
                'data': staff_serializer.data
            }, status=status.HTTP_200_OK)

        except Staff.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Staff not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
