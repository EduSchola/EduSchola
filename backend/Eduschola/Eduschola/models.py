from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError


class School(models.Model):
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    address = models.TextField()
    country = models.TextField(default='')
    state = models.TextField(default='')
    city = models.TextField(default='')
    lga = models.TextField(default='')


    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True)  # Many-to-One relationship with staff model (Teacher)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)  # Many-to-One relationship with School model

    def __str__(self):
        return self.name

class Grade(models.Model):
    grade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    grade_name = models.CharField(max_length=50, default='') #Indicating grade level of student
    grade_description = models.TextField(default='')
    
    def __str__(self):
        return f"Grade {self.grade_id} - Staff: {self.staff}, Student: {self.student}, Course: {self.course}"
    
    def delete(self, *args, **kwargs):
        # Delete 
        super().delete(*args, **kwargs)
    
class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=uuid.uuid4)  # Many-to-One relationship with Course model
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default=uuid.uuid4)  # Many-to-One relationship with Grade model. Indicating the grade level of the assignment
    
        
    def __str__(self):
        return self.title
    
    def clean(self):
        # Validate that the issue_date is not in the past
        if self.issue_date and self.issue_date < timezone.now():
            raise ValidationError('Issue date cannot be in the past.')

        # Validate that the due_date is after the issue_date
        if self.issue_date and self.due_date and self.due_date < self.issue_date:
            raise ValidationError('Due date cannot be before the issue date.')
    
    def save(self, *args, **kwargs):
        self.clean() 
        return super().save(*args, **kwargs)

class Announcement(models.Model):
    announcement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)  # Many-to-One relationship with Course model (optional)
    is_school_wide = models.BooleanField(default=False)  # Indicates if the announcement is school-wide

    def __str__(self):
        return self.title

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, related_name='student_user')
    date_of_birth = models.DateField()
    phone_number = models.TextField()
    address = models.TextField()
    parent = models.ForeignKey('Parent', on_delete=models.SET_NULL, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Many-to-One relationship with School model    

    def delete(self, *args, **kwargs):
        # Delete associated User instance
        if self.user:
            self.user.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Staff(models.Model):
    staff_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, related_name='staff_user')
    phone = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    address = models.TextField()
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('Course', blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    password = models.TextField(default='')
    staff_role = models.CharField(max_length=255)  # Add staff role field

    def delete(self, *args, **kwargs):
        # Delete associated User instance
        if self.user:
            self.user.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Parent(models.Model):
    parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, related_name='parent_user')    
    phone = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    address = models.TextField()

    def delete(self, *args, **kwargs):
        # Delete associated User instance
        if self.user:
            self.user.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ROLES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('parent', 'Parent'),
    )

    role = models.CharField(max_length=10, choices=ROLES)
    school = models.ForeignKey(School, on_delete=models.SET_NULL,
                               null=True)  # Foreign Key relationship with School model
        # Add related_name to the groups field
    groups = models.ManyToManyField(Group, related_name='users')

    # Add related_name to the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users',
        verbose_name='user permissions',
        blank=True,
    )

    def __str__(self):
        return self.username

class CourseRegistration(models.Model):
    registration_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)  
    session = models.CharField(max_length=10)  # e.g., '2023-2024'
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student} - {', '.join(str(course) for course in self.courses.all())} ({self.session})"