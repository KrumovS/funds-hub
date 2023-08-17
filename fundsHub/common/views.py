from django.shortcuts import render

from fundsHub.projects.models import Project


def home(request):
    projects = Project.objects.order_by('-project_created_on')[:3]
    return render(request, template_name='common/index.html', context={'projects': projects})


def our_mission(request):
    return render(request, template_name='common/our-mission.html')

