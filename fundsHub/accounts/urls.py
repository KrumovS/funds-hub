from django.urls import path

from fundsHub.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    #path('profile/<int:pk>/', include([]))

]