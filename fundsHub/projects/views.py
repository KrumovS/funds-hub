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
    project = Project.objects.get(pk=pk)
    progress_percentage = 0
    if project.funding_goal > 0:
        progress_percentage = (project.donated / project.funding_goal) * 100

    completeness = ProjectCompleteness.objects.filter(min_percentage__lte=progress_percentage,
                                                      max_percentage__gt=progress_percentage).first()
    if completeness is None:
        default_completeness = ProjectCompleteness.objects.filter(min_percentage=0).first()
        completeness_description = default_completeness.description if default_completeness else "No description available"
    else:
        completeness_description = completeness.description

    context = {
        "project": project,
        "progress_percentage": progress_percentage,
        "completeness_description": completeness_description,
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
        return HttpResponseForbidden("You don't have permission to edit this project")

    if request.method == 'POST':
        form = ProjectEditForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            url = reverse(viewname='my-projects', args=[project.user.pk])
            return HttpResponseRedirect(url)
    else:
        form = ProjectEditForm(instance=project)

    return render(request, template_name='projects/edit-project.html', context={'form': form})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this project")

    if request.method == 'POST':
        project.delete()
        url = reverse(viewname='my-projects', args=[project.user.pk])
        return HttpResponseRedirect(url)

    return render(request, template_name='projects/delete-project.html', context={'project': project})


@login_required
def donate(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        amount = int(request.POST.get('amount', '0.00'))

        # Update project's donation amount
        project.donated += amount
        project.save()

        # Update user's total donated amount
        request.user.amount_donated += int(
            amount)  # Assuming `amount_donated` stores the value in cents or similar to avoid float issues.
        request.user.save()

        # Save the donation record for the user
        donation = Donation(user=request.user, project=project, amount=amount)
        donation.save()

        update_user_account_level(request.user)

        messages.success(request, f'Thank you for your donation of ${amount}!')

    return redirect('home')


def update_user_account_level(user):
    total_donations = user.amount_donated

    try:
        new_level = AccountLevel.objects.get(min_amount__lte=total_donations, max_amount__gte=total_donations)
    except AccountLevel.DoesNotExist:
        new_level = None

    if new_level:
        user.account_level = new_level
        user.save()
