
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .serializers import UserSerializer, StudentSerializer, ParentUserSerializer, ParentSerializer, StaffSerializer
from .models import User, Student, Staff, Parent

# Create your views here.

# Student View
class StudentView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def create(self, request, *args, **kwargs):
        student_data = request.data.copy()
        parent_data = student_data.pop('parent')
        user_data = student_data.pop('user')

        user_serializer = UserSerializer(data=user_data)
        parent_user_serializer = UserSerializer(data=parent_data['user'])
        parent_serializer = ParentSerializer(data=parent_data)
        student_serializer = StudentSerializer(data=student_data)

        if (
            user_serializer.is_valid(raise_exception=True)
            and parent_user_serializer.is_valid(raise_exception=True)
            and parent_serializer.is_valid(raise_exception=True)
            and student_serializer.is_valid(raise_exception=True)
        ):
            user = user_serializer.save()

            parent_user = parent_user_serializer.save()
            parent_data['user'] = parent_user.user_id
            parent_serializer.save(user=parent_user)

            student_data['user'] = user.user_id
            student_data['parent'] = parent_serializer.instance.parent_id
            student_serializer.save(user=user, parent=parent_serializer.instance)

            return Response({
                'success': True,
                'data': student_serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'data': {
                'user': user_serializer.errors,
                'parent_user': parent_user_serializer.errors,
                'parent': parent_serializer.errors,
                'student': student_serializer.errors,
            }
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        student = self.get_object()
        student_serializer = StudentSerializer(instance=student, data=request.data, partial=True)


        if student_serializer.is_valid(raise_exception=True):
            student_serializer.save()

            user_data = request.data.get('user')
            if user_data:
                user = student.user
                user_serializer = UserSerializer(instance=user, data=user_data, partial=True)

                if user_serializer.is_valid(raise_exception=True):
                    user_serializer.save()

            return self.update(request, *args, **kwargs)

        return Response({
            'success': False,
            'data': student_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete student details
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'message': 'Student deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    # Retrieve students details by student_id
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

    # Retrieve all students details
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

    # # Retrieve all students details
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     student_serializer = self.get_serializer(queryset, many=True)

    #     return Response({
    #         'success': True,
    #         'data': student_serializer.data
    #     }, status=status.HTTP_200_OK)


class ParentView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView, generics.ListAPIView):

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = 'parent_id'


    # Modify parent details
    def patch(self, request, *args, **kwargs):
        parent_data = request.data.copy()
        user_data = parent_data.pop('user', None)
        parent = self.get_object()
        parent_serializer = self.get_serializer(instance=parent, data=parent_data, partial=True)

        if parent_serializer.is_valid(raise_exception=True):
            parent_serializer.save()  # Update the Parent instance

            if user_data:
                user = parent.user
                user_serializer = UserSerializer(instance=user, data=user_data, partial=True)

                if user_serializer.is_valid(raise_exception=True):
                    user_serializer.save()  # Update the User instance

            return Response({
                'success': True,
                'data': parent_serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'data': parent_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Delete parent details and related user details
    def delete(self, request, *args, **kwargs):
        parent = self.get_object()
        parent.delete()

        return Response({
            'success': True,
            'message': 'Parent deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    # Retrieve Parent details by parent_id
    def get(self, request, *args, **kwargs):
        try:
            parent = self.get_object()
        except NotFound:
            return Response({
                'success': False,
                'message': 'Parent not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        parent_serializer = self.get_serializer(instance=parent)

        return Response({
            'success': True,
            'data': parent_serializer.data
        }, status=status.HTTP_200_OK)

    # Retrieve all parents details
    def list(self, request, *args, **kwargs):
        try:
            parents = self.get_queryset()
            parent_serializer = self.get_serializer(instance=parents, many=True)

            return Response({
                'success': True,
                'data': parent_serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

# Staff Views
class StaffView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = StaffSerializer

    # Create new staff
    def create(self, request, *args, **kwargs):
        try:
            staff_data = request.data.copy()
            user_data = staff_data.pop('user')

            user_serializer = UserSerializer(data=user_data)
            staff_serializer = self.get_serializer(data=staff_data)

            if (
                user_serializer.is_valid(raise_exception=True)
                and staff_serializer.is_valid(raise_exception=True)
            ):
                user = user_serializer.save()  # Save the User instance

                staff_data['user'] = user.user_id  # Set the user_id in staff data
                staff_serializer.save(user=user)  # Save the Staff instance

                return Response({
                    'success': True,
                    'data': staff_serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                'success': False,
                'data': {
                    'user': user_serializer.errors,
                    'staff': staff_serializer.errors,
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Modify staff details
    def patch(self, request, *args, **kwargs):
        try:
            staff_data = request.data.copy()
            user_data = staff_data.pop('user', None)

            staff = self.get_object()
            staff_serializer = self.get_serializer(instance=staff, data=staff_data, partial=True)

            if staff_serializer.is_valid(raise_exception=True):
                staff_serializer.save()  # Update the Staff instance

                if user_data:
                    user = staff.user
                    user_serializer = UserSerializer(instance=user, data=user_data, partial=True)

                    if user_serializer.is_valid(raise_exception=True):
                        user_serializer.save()  # Update the User instance

                return Response({
                    'success': True,
                    'data': staff_serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                'success': False,
                'data': staff_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Staff.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Staff not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Retrieve Staff details by staff_id
    def get(self, request, staff_id):
        try:
            staff = get_object_or_404(Staff, staff_id=staff_id)
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
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Retrieve all staff details
    def list(self, request):
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
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
