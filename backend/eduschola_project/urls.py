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
from eduschola_project.edusch_app.views import StudentViewSet, ParentViewSet, StaffViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    # Student URLs
    path('students/', StudentViewSet.as_view({'post': 'create_student'}), name='student-create'),
    path('students/<uuid:student_id>/', StudentViewSet.as_view({'delete': 'delete_student'}), name='student-details'),
    path('students/<uuid:student_id>/', StudentViewSet.as_view({'patch': 'modify_student'}), name='student-details'),
    path('students/<uuid:student_id>/', StudentViewSet.as_view({'get': 'get_student'}), name='modify-student-details'),
    path('students/', StudentViewSet.as_view({'get': 'get_all_students'}), name='all-student'),
    
    # Parent URLs
    path('parents/<uuid:parent_id>/', ParentViewSet.as_view({'patch': 'modify_parent'}), name='parent-details'),
    path('parents/<uuid:parent_id>/', ParentViewSet.as_view({'delete': 'delet_-parent'}), name='parent-details'),
    # path('parents/', ParentViewSet.as_view({'post': 'create_parent'}), name='create-parents'),
    path('parents/<uuid:parent_id>/', ParentViewSet.as_view({'get': 'get_parent'}), name='modify-staff-details'),
    path('parents/', ParentViewSet.as_view({'get': 'get_all_parent'}), name='all-staff'),

    # Staff URLs     
    path('staff/', StaffViewSet.as_view({'post': 'create_staff'}), name='create-staff'),
    path('staff/<uuid:staff_id>/', StaffViewSet.as_view({'get': 'get_staff'}), name='staff-details'),
    path('staff/<uuid:staff_id>/', StaffViewSet.as_view({'delete': 'delete_staff'}), name='delete-staff-details'),
    path('staff/<uuid:staff_id>/', StaffViewSet.as_view({'patch': 'modify_staff'}), name='modify-staff-details'),
    path('staff/', StaffViewSet.as_view({'get': 'get_all_staff'}), name='all-staff'),
       
        
]
