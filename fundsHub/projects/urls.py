from django.urls import path

from fundsHub.projects import views

urlpatterns = [
    path('all-projects/', views.browse_projects, name='browse-projects'),
    path('my-projects/<int:pk>/', views.user_projects, name='my-projects'),
    path('project/<int:pk>/', views.project_detail, name='project-detail'),
    path('project/create/', views.create_project, name='create-project'),
    path('project/<int:pk>/edit', views.edit_project, name='edit-project'),
    path('project/<int:pk>/delete', views.delete_project, name='delete-project'),
    path('project/<int:pk>/donate', views.donate, name='donate')

]
