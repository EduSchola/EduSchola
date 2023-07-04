from django.contrib import admin
from .models import User, Student, Staff, Parent, School, Course

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Parent)
admin.site.register(School)
admin.site.register(Course)