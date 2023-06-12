"""
URL configuration for eduschola_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eduschola_project.edusch_app.views import StudentListCreateView, StudentRetrieveUpdateDestroyView, \
    create_or_list_all_courses, get_update_delete_courseDetail
from eduschola_project.edusch_app.views import InstructorListCreateView, InstructorRetrieveUpdateDestroyView
from eduschola_project.edusch_app.views import ParentListCreateView, ParentRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    # Student URLs
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<uuid:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),

    # Instructor URLs
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructors/<uuid:pk>/', InstructorRetrieveUpdateDestroyView.as_view(),
         name='instructor-retrieve-update-destroy'),

    # Parent URLs
    path('parents/', ParentListCreateView.as_view(), name='parent-list-create'),
    path('parents/<uuid:pk>/', ParentRetrieveUpdateDestroyView.as_view(), name='parent-retrieve-update-destroy'),

    # Course URLs
    path('course/', create_or_list_all_courses, name='course-create-list'),
    path('course/<uuid:pk>/', get_update_delete_courseDetail, name='course-get-detail-update-delete'),
]