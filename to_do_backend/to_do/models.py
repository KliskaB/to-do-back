from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=LOW,
    )
    complited = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title