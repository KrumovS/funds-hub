from django.shortcuts import render


def browse_projects(request):
    return render(request, template_name='projects/browse-projects.html')

