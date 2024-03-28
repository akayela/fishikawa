from django.db import models

# Create your models here.
class Task(models.Model):
    date = models.DateField(auto_now_add=True)
    assignee = models.CharField(max_length=200)
    assignment = models.CharField(max_length=200)
    due = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
        ('Incomplete', 'Incomplete'),
    )
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pending')
    PRIMARY_ANALYSIS_CHOICES = (
        ('Manpower', 'Manpower'),
        ('Process(es)', 'Process(es)'),
        ('Money', 'Money'),
        ('Machinery', 'Machinery'),
        ('Matrices', 'Matrices'),
        ('Culture', 'Culture'),
    )
    primary_cause = models.CharField(max_length=200, choices=PRIMARY_ANALYSIS_CHOICES, default='Process(es)', blank=True, null=True)
    problem = models.CharField(max_length=255, blank=True, null=True)
    why1 = models.CharField(max_length=255, blank=True, null=True)
    why2 = models.CharField(max_length=255, blank=True, null=True) 
    why3 = models.CharField(max_length=255, blank=True, null=True)
    why4 = models.CharField(max_length=255, blank=True, null=True)
    root_cause = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.assignment
