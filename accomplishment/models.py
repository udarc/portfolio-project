from django.db import models
from django.urls import reverse
# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return reverse('job-detail', kwargs={'job_id': self.pk})
