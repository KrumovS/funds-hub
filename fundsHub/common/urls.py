from django.urls import path

from fundsHub.common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('our-mission/', views.our_mission, name='our-mission'),
    path('get-started/', views.get_started, name='get-started'),

]
