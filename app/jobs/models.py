from django.db import models
from common.models import BaseModel

# Choices for Job Types
JOB_TYPE_CHOICES = [
    ('FT', 'Full-Time'),
    ('PT', 'Part-Time'),
    ('FR', 'Freelance'),
    ('CT', 'Contract'),
    ('IN', 'Internship'),
    ('VT', 'Volunteer'),
]

PAY_FREQUENCY_CHOICES = [
    ('SA', 'Salary'),
    ('HR', 'Hourly'),
    ('PD', 'Per Diem'),
    ('OT', 'One-time'),
    ('NA', 'N/A'),
]


class Job(BaseModel):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # Job or company's location
    is_remote = models.BooleanField(default=False)  # Flag for remote positions
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default='FT')
    description = models.TextField()
    pay_range = models.CharField(max_length=100, blank=True, null=True)
    pay_frequency = models.CharField(max_length=2, choices=PAY_FREQUENCY_CHOICES, default='SA')

    application_email = models.EmailField(blank=True, null=True)
    application_link = models.URLField(blank=True, null=True)
