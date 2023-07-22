from django.urls import path

from fundsHub.projects import views

urlpatterns = [
    path('', views.browse_projects, name='browse-projects'),

]