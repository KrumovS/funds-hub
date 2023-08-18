from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from fundsHub.accounts.models import AccountLevel
from fundsHub.projects.forms import CreateProjectForm, ProjectEditForm
from fundsHub.projects.models import Project, Donation, ProjectCompleteness


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


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    progress_percentage = 0
    today = date.today()

    if project.funding_goal > 0:
        progress_percentage = (project.donated / project.funding_goal) * 100

    completeness = ProjectCompleteness.objects.filter(min_percentage__lte=progress_percentage,
                                                      max_percentage__gt=progress_percentage).first()

    completeness_description = completeness.description

    delta = project.project_end_date - today
    days_remaining = max(0, delta.days)
    project_active = days_remaining > 0

    context = {
        "project": project,
        "progress_percentage": progress_percentage,
        "completeness_description": completeness_description,
        "days_remaining": days_remaining,
        "project_active": project_active
    }
    return render(request, template_name='projects/project-details.html', context=context)


@login_required
def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')
    else:
        form = CreateProjectForm()
    return render(request, template_name='projects/create-project.html', context={'form': form})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.user != request.user:
        return redirect('project-detail', pk=project.pk)

    today = date.today()
    if project.project_end_date <= today:
        return redirect('project-detail', pk=project.pk)

    if request.method == 'POST':
        form = ProjectEditForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('project-detail', pk=project.pk)
    else:
        form = ProjectEditForm(instance=project)

    return render(request, template_name='projects/edit-project.html', context={'form': form, 'project': project})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.user != request.user:
        return redirect('project-detail', pk=project.pk)

    today = date.today()
    if project.project_end_date <= today:
        return redirect('project-detail', pk=project.pk)

    if request.method == 'POST':
        project.delete()
        url = reverse(viewname='my-projects', args=[project.user.pk])
        return HttpResponseRedirect(url)

    return render(request, template_name='projects/delete-project.html', context={'project': project})


@login_required
def donate(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        try:
            amount = int(request.POST.get('amount'))
        except ValueError:
            messages.error(request, message='Please enter a valid donation amount.')
            return redirect('project-detail', pk=project.pk)

        if amount <= 0:
            messages.error(request, message='Please enter a positive donation amount.')
            return redirect('project-detail', pk=project.pk)

        project.donated += amount
        project.save()

        request.user.amount_donated += amount
        request.user.save()

        donation = Donation(user=request.user, project=project, amount=amount)
        donation.save()

        messages.success(request, message=f'Thank you for your donation of {amount}!')

    return redirect('project-detail', pk=project.pk)

