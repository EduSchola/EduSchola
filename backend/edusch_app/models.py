from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
    administrator = models.OneToOneField('User', on_delete=models.CASCADE, related_name='school_administrator')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)  # Many-to-One relationship with User model (Teacher)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model

    def __str__(self):
        return self.name

class CourseEnrollment(models.Model):
    student = models.ForeignKey('User', on_delete=models.CASCADE)  # Many-to-One relationship with User model (Student)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Many-to-One relationship with Course model

    def __str__(self):
        return f"Enrollment ID: {self.id}, Student: {self.student.username}, Course: {self.course.name}"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Many-to-One relationship with Course model

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)  # Many-to-One relationship with Course model (optional)
    is_school_wide = models.BooleanField(default=False)  # Indicates if the announcement is school-wide

    def __str__(self):
        return self.title


class Grade(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='student_user')
    date_of_birth = models.DateField()
    phone_number = models.TextField()
    address = models.TextField()
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)  # Many-to-One relationship with Class model

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=255)
    instructors = models.ManyToManyField('Instructor')
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='instructor_user')
    qualification = models.CharField(max_length=255)
    contact_information = models.TextField()
    address = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    grades = models.ManyToManyField(Grade)

    def __str__(self):
        return self.user.username

class Parent(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='parent_user')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_information = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLES)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)  # Foreign Key relationship with School model

    # Relationships
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='user_student')
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name='user_parent')
    instructor = models.OneToOneField(Instructor, on_delete=models.CASCADE, related_name='user_instructor')
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
