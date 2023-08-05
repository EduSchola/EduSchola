from django.contrib import admin
from .models import Assignment, School, Student, Staff, Parent

# Register your models here.
admin.site.register(Assignment)
admin.site.register(School)
admin.site.register(Student)