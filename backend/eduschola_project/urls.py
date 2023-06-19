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

from eduschola_project.edusch_app.views import StudentView, ParentView, StaffView


urlpatterns = [
    path('admin/', admin.site.urls),
    # Student URLs

    path('students/', StudentView.as_view(), name='student-list'),
    path('students/<uuid:pk>/', StudentView.as_view(), name='student-detail'),

    # Parent URLs
    path('parents/', ParentView.as_view(), name='parent-list'),
    path('parents/<uuid:pk>/', ParentView.as_view(), name='parent-detail'),

    # Staff URLs     
    path('staff/', StaffView.as_view(), name='staff-list'),
    path('staff/<uuid:pk>/', StaffView.as_view(), name='staff-detail'),

]
