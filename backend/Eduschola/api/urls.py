from django.urls import path
from django.views.generic.base import RedirectView
from .endpoints.students import StudentView, StudentRetrieveUpdateDestroyView
from .endpoints.parents import ParentView, ParentListView
from .endpoints.staff import StaffView, StaffRetrieveView
from .endpoints.grade import GradeView, GradeDeleteUpdateRetrieveView
from .endpoints.course import CreateCourseApiView, ListAllCourseApiView, DetailUpdateDeleteCourseApiView
urlpatterns = [
    # ---------------student url start------------------------
    path('students/', StudentView.as_view(), name='student-list'),
    path('students/<uuid:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve'),
    # ---------------student url end--------------------------

    # ---------------Parent url start--------------------------
    path('parents/', ParentListView.as_view(), name='parent-list'),
    path('parents/<uuid:pk>/', ParentView.as_view(), name='parent-retrieve'),
    # ---------------Parent url end----------------------------

    # ---------------staff url start--------------------------
    path('staff/', StaffView.as_view(), name='staff-list'),
    path('staff/<uuid:pk>/', StaffRetrieveView.as_view(), name='staff-retrieve'),
    # ---------------staff url end----------------------------

    # ---------------grade url start--------------------------
    path('grade/', GradeView.as_view(), name='grade-list'),
    path('grade/<uuid:pk>/', GradeDeleteUpdateRetrieveView.as_view(), name='grade-retrieve'),
    # ---------------grade url end-------------------------------

    # ---------------course url start--------------------------
    path('courses/create', CreateCourseApiView.as_view(), name='course-list'),
    path('courses/<uuid:pk>/', DetailUpdateDeleteCourseApiView.as_view(), name='course-retrieve'),
    # ---------------course url end-------------------------------

    path('' , RedirectView.as_view(url='/'))
]
