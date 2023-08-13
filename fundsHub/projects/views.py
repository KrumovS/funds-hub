from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from fundsHub.projects.forms import CreateProjectForm
from fundsHub.projects.models import Project


def browse_projects(request):
    projects = Project.objects.all()
    return render(request, template_name='projects/browse-projects.html', context={'projects': projects})


@login_required
def user_projects(request, pk):
    if request.user.is_authenticated:
        projects = request.user.projects.all()
    else:
        projects = []

    return render(request, template_name='projects/user-projects.html', context={'projects': projects})


@login_required
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project,
    }
    return render(request, template_name='projects/project-details.html', context=context)


@login_required
def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')
    else:
        form = CreateProjectForm()
    return render(request, template_name='projects/create-project.html', context={'form': form})



