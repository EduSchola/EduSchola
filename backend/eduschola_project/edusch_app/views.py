from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import generics
from .serializers import UserSerializer, StudentSerializer, ParentUserSerializer, ParentSerializer, StaffSerializer
from .models import User, Student, Staff, Parent
# Create your views here.

# Student View
class StudentViewSet(viewsets.ViewSet):
    # create student and parent
    @action(detail=True, methods=['POST'], name='create-student')
    def create_student(self, request):
        student_data = request.data.copy()
        parent_data = student_data.pop('parent')
        user_data = student_data.pop('user')

        user_serializer = UserSerializer(data=user_data)
        parent_user_serializer = UserSerializer(data=parent_data['user'])  # Use UserSerializer for parent user data
        parent_serializer = ParentSerializer(data=parent_data)
        student_serializer = StudentSerializer(data=student_data)

        if (
            user_serializer.is_valid(raise_exception=True)
            and parent_user_serializer.is_valid(raise_exception=True)
            and parent_serializer.is_valid(raise_exception=True)
            and student_serializer.is_valid(raise_exception=True)
        ):
            user = user_serializer.save()  # Save the User instance

            parent_user = parent_user_serializer.save()  # Save the ParentUser instance
            parent_data['user'] = parent_user.user_id  # Set the user_id in parent data            
            parent_serializer.save(user=parent_user)  # Save the Parent instance

            student_data['user'] = user.user_id  # Set the user_id in student data
            student_data['parent'] = parent_serializer.instance.parent_id
            student_serializer.save(user=user, parent=parent_serializer.instance)  # Save the Student instance

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

    # Modify student
    @action(detail=True, methods=['PATCH'], name='modify-student')
    def patch(self, request, student_id):
        student_data = request.data.copy()
        user_data = student_data.pop('user', None)

        student = Student.objects.get(student_id=student_id)
        student_serializer = StudentSerializer(instance=student, data=student_data, partial=True)

        if student_serializer.is_valid(raise_exception=True):
            student_serializer.save()  # Update the Student instance

            if user_data:
                user = student.user
                user_serializer = UserSerializer(instance=user, data=user_data, partial=True)

                if user_serializer.is_valid(raise_exception=True):
                    user_serializer.save()  # Update the User instance

            return Response({
                'success': True,
                'data': student_serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'data': student_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete student details
    @action(detail=True, methods=['DELETE'], name='delete-student')
    def delete(self, request, student_id):
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Student not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        student.delete()

        return Response({
            'success': True,
            'message': 'Student deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    # Retrieve students details by student_id
    @action(detail=True, methods=['GET'], name='get-student-details')
    def get_student(self, request, student_id):
        student = get_object_or_404(Student, student_id=student_id)
        student_serializer = StudentSerializer(instance=student)
        user_serializer = UserSerializer(instance=student.user)

        return Response({
            'success': True,
            'data': {
                'student': student_serializer.data,
                'user': user_serializer.data
            }
        }, status=status.HTTP_200_OK)

    # Retrieve all students details
    @action(detail=True, methods=['GET'], name='get-all-student')
    def get_all_students(self, request):
        students = Student.objects.all()
        student_serializer = StudentSerializer(instance=students, many=True)

        return Response({
            'success': True,
            'data': student_serializer.data
        }, status=status.HTTP_200_OK)


# Parent Views
class ParentViewSet(viewsets.ViewSet):
    # Modify parent details
    @action(detail=True, methods=['PATCH'], name='modify-parent')
    def patch(self, request, parent_id):
        parent_data = request.data.copy()
        user_data = parent_data.pop('user', None)

        try:
            parent = Parent.objects.get(parent_id=parent_id)
        except Parent.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Parent not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        parent_serializer = ParentSerializer(instance=parent, data=parent_data, partial=True)

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

    # Delete parent details and related user deails
    @action(detail=True, methods=['DELETE'], name='delete-parent')
    def delete(self, request, parent_id):
        try:
            parent = Parent.objects.get(parent_id=parent_id)
        except Parent.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Parent not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        parent.delete()

        return Response({
            'success': True,
            'message': 'Parent deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    # Retrieve Parent details by parent_id
    @action(detail=True, methods=['GET'], name='get-parent-details')
    def get_parent(self, request, parent_id):
        parent = get_object_or_404(Parent, parent_id=parent_id)
        parent_serializer = ParentUserSerializer(instance=parent)

        return Response({
            'success': True,
            'data': parent_serializer.data
        }, status=status.HTTP_200_OK)

    # Retrieve all parents details 
    @action(detail=True, methods=['GET'], name='get-all-parent-details')
    def get_all_parent(self, request):
        parents = Parent.objects.all()
        parent_serializer = ParentSerializer(instance= parents, many=True)

        return Response({
            'success': True,
            'data': parent_serializer.data
        }, status=status.HTTP_200_OK)

# Staff Views
class StaffViewSet(viewsets.ViewSet):
    # create new staff
    @action(detail=True, methods=['POST'], name='create-staff')
    def create_staff(self, request):
        staff_data = request.data.copy()
        user_data = staff_data.pop('user')

        user_serializer = UserSerializer(data=user_data)
        staff_serializer = StaffSerializer(data=staff_data)

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

    # Modify staff details
    @action(detail=True, methods=['PATCH'], name='modify-staff')
    def patch(self, request, staff_id):
        staff_data = request.data.copy()
        user_data = staff_data.pop('user', None)

        try:
            staff = Staff.objects.get(staff_id=staff_id)
        except Staff.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Staff not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        staff_serializer = StaffSerializer(instance=staff, data=staff_data, partial=True)

        if staff_serializer.is_valid(raise_exception=True):
            staff_serializer.save()  # Update the Parent instance

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

    # Delete staff details and related user deails
    @action(detail=True, methods=['DELETE'], name='delete-staff')
    def delete(self, request, staff_id):
        try:
            staff = Staff.objects.get(staff_id=staff_id)
        except Staff.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Staff not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        staff.delete()

        return Response({
            'success': True,
            'message': 'Staff deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

    # Retrieve Staff details by staff_id
    @action(detail=True, methods=['GET'], name='Get Staff')
    def get_staff(self, request, staff_id):
        staff = get_object_or_404(Staff, staff_id=staff_id)
        staff_serializer = StaffSerializer(instance=staff)

        return Response({
            'success': True,
            'data': staff_serializer.data
        }, status=status.HTTP_200_OK)

    # Retrieve all staff details
    @action(detail=False, methods=['GET'], name='Get All Staff') 
    def get_all_staff(self, request):
        staff = Staff.objects.all()
        staff_serializer = StaffSerializer(instance= staff, many=True)

        return Response({
            'success': True,
            'data': staff_serializer.data
        }, status=status.HTTP_200_OK)