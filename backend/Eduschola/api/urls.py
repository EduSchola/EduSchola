from django.urls import path
from django.views.generic.base import RedirectView
from .endpoints.students import StudentView, StudentRetrieveUpdateDestroyView
from .endpoints.parents import ParentView, ParentCreateListView
from .endpoints.staff import StaffView, StaffRetrieveView
from .endpoints.grade import GradeListCreateView, GradeRetrieveUpdateDestroyView
from .endpoints.course import CreateCourseApiView, ListAllCourseApiView, DetailUpdateDeleteCourseApiView
from .endpoints.school import CreateSchoolApiView
from .endpoints.assignment import CreateAssignmentApiView, ListAssignmentApiView, AssignmentApiView
from .endpoints.announcement import CreateAnnouncementApiView, ListAnnouncementApiView, AnnouncementApiView

urlpatterns = [
    # ---------------student url start------------------------
    path('students/', StudentView.as_view(), name='student-list'),
    path('students/<uuid:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve'),
    # ---------------student url end--------------------------

    # ---------------Parent url start--------------------------
    path('parents/', ParentCreateListView.as_view(), name='parent-list'),
    path('parents/<uuid:pk>/', ParentView.as_view(), name='parent-retrieve'),
    # ---------------Parent url end----------------------------

    # ---------------staff url start--------------------------
    path('staff/', StaffView.as_view(), name='staff-list'),
    path('staff/<uuid:pk>/', StaffRetrieveView.as_view(), name='staff-retrieve'),
    # ---------------staff url end----------------------------

    # ---------------grade url start--------------------------
    path('grades/', GradeListCreateView.as_view(), name='grade-list'),
    path('grades/<uuid:pk>/', GradeRetrieveUpdateDestroyView.as_view(), name='grade-retrieve'),
    # ---------------grade url end-------------------------------

    # ---------------course url start--------------------------
    path('courses/', CreateCourseApiView.as_view(), name='course-list'),
    path('courses/list/', ListAllCourseApiView.as_view(), name='list-all-courses'),
    path('courses/<uuid:pk>/', DetailUpdateDeleteCourseApiView.as_view(), name='course-retrieve'),
    # ---------------course url end-------------------------------

    #-----------------school url start----------------------------
    path('schools/create/', CreateSchoolApiView.as_view(), name='schoool-create'),    
    # ---------------school url end-------------------------------

    #-----------------assignment url start----------------------------
    path('assignment/create/', CreateAssignmentApiView.as_view(), name='assignment-create'),
    path('assignment/list/', ListAssignmentApiView.as_view(), name='assignment-list'),
    path('assignment/<uuid:pk>/', AssignmentApiView.as_view(), name='assignment-retrieve-deleye-update'),
    # ---------------assignment url end-------------------------------

    #-----------------announcement url start----------------------------
    path('announcement/create/', CreateAnnouncementApiView.as_view(), name='announcement-create'),
    path('announcement/list/', ListAnnouncementApiView.as_view(), name='announcement-list'),
    path('announcement/<uuid:pk>/', AnnouncementApiView.as_view(), name='announcement-retrieve-deleye-update'),
    # ---------------announcement url end-------------------------------

    path('' , RedirectView.as_view(url='/'))
]
