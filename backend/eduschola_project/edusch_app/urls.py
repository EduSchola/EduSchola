from django.urls import path, include
from .views import *


urlpatterns =[
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<uuid:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),

    # Instructor URLs
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructors/<uuid:pk>/', InstructorRetrieveUpdateDestroyView.as_view(),
         name='instructor-retrieve-update-destroy'),

    # Parent URLs
    path('parents/', ParentListCreateView.as_view(), name='parent-list-create'),
    path('parents/<uuid:pk>/', ParentRetrieveUpdateDestroyView.as_view(), name='parent-retrieve-update-destroy'),

    path('announcements/', CreateAnnouncementView.as_view(), name='announcements-list-create')
]