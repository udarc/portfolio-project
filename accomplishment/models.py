from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models


# class TimestampMixin(models.Model):
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at =  models.DateTimeField(auto_now=True)

# class Technology(TimestampMixin):
    
# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     technology = models.CharField(max_length=20)
#     image = models.FilePathField(path="/img")


class Job(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return reverse('job-detail', kwargs={'job_id': self.pk})
