from django.shortcuts import render


def home(request):
    return render(request, template_name='common/index.html')


def our_mission(request):
    return render(request, template_name='common/our-mission.html')


def get_started(request):
    return render(request, template_name='common/get-started.html')