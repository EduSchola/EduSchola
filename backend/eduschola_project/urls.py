from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edusch_app/', include('eduschola_project.edusch_app.urls'))
]
