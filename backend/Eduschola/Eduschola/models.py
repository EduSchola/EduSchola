from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError


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
