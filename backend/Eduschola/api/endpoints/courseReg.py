from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers import CourseRegistrationSerializer
from Eduschola.models import CourseRegistration

class CreateCourseRegistrationApiView(generics.CreateAPIView):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer

    def perform_create(self, serializer):
        student_id = self.request.data.get('student')
        session = self.request.data.get('session')
        selected_course_ids = self.request.data.getlist('courses')

        # Validate that a student registers a minimum of 9 courses
        existing_registrations = CourseRegistration.objects.filter(student=student_id, session=session)
        if existing_registrations.count() + len(selected_course_ids) < 9:
            return Response({
                'error': 'A student must register a minimum of 9 courses per session.'
                }, status=status.HTTP_400_BAD_REQUEST)

        # Store the course IDs as a list in the course field
        serializer.save(course=selected_course_ids)

class ListStudentCoursesBySessionApiView(generics.ListAPIView):
    serializer_class = CourseRegistrationSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        session = self.kwargs['session']
        return CourseRegistration.objects.filter(student=student_id, session=session)

class UpdateStudentCoursesApiView(generics.UpdateAPIView):
    serializer_class = CourseRegistrationSerializer

    def get_object(self):
        student_id = self.kwargs['student_id']
        session = self.kwargs['session']
        return CourseRegistration.objects.get(student=student_id, session=session)

    def perform_update(self, serializer):
        selected_course_ids = self.request.data.getlist('courses')

        # Validate that a student cannot have less than 9 courses
        if len(selected_course_ids) < 9:
            return Response({
                'error': 'A student must register a minimum of 9 courses.'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(courses=selected_course_ids)