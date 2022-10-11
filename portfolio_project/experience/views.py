from django.shortcuts import render
from .models import Job

def experience(request):
    jobs = Job.objects
    return render(request, 'experience.html',{'jobs':jobs})

