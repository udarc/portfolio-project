from django.shortcuts import render, get_object_or_404

from .models import Job 


def homepage(request):
    jobs = Job.objects.all()
    return render(request,'accomplishment/home.html',{'jobs':jobs})

def job_detail(request, job_id):
    job_detail = get_object_or_404(Job,pk=job_id)
    return render(request, 'accomplishment/job_detail.html', {'job':job_detail})
