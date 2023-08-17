from django.urls import path, include

from fundsHub.projects import views

project_patterns = [
    path('<int:pk>/', views.project_detail, name='project-detail'),
    path('create/', views.create_project, name='create-project'),
    path('<int:pk>/edit/', views.edit_project, name='edit-project'),
    path('<int:pk>/delete/', views.delete_project, name='delete-project'),
    path('<int:pk>/donate/', views.donate, name='donate'),
]

urlpatterns = [
    path('all-projects/', views.browse_projects, name='browse-projects'),
    path('my-projects/<int:pk>/', views.user_projects, name='my-projects'),
    path('project/', include(project_patterns)),
]
