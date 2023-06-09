from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
import uuid


# Create your models here.

class School(models.Model):
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_information = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)  # Many-to-One relationship with User model (Teacher)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model

    def __str__(self):
        return self.name


class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Many-to-One relationship with Course model

    def __str__(self):
        return self.title


class Announcement(models.Model):
    announcement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, null=True, blank=True,
                               on_delete=models.CASCADE)  # Many-to-One relationship with Course model (optional)
    is_school_wide = models.BooleanField(default=False)  # Indicates if the announcement is school-wide

    def __str__(self):
        return self.title


class Grade(models.Model):
    grade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='student_user')
    date_of_birth = models.DateField()
    phone_number = models.TextField()
    address = models.TextField()
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)  # Many-to-One relationship with Class model

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    instructor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='instructor_user')
    qualification = models.CharField(max_length=255)
    tel = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    address = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Course')
    grades = models.ManyToManyField(Grade)

    def __str__(self):
        return self.user.username


class Parent(models.Model):
    parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='parent_user')
    tel = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLES)
    school = models.ForeignKey(School, on_delete=models.SET_NULL,
                               null=True)  # Foreign Key relationship with School model

    # Add related_name to the groups field
    groups = models.ManyToManyField(Group, related_name='custom_user_set')

    # Add related_name to the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        verbose_name='user permissions',
        blank=True,
    )

    def __str__(self):
        return self.username
