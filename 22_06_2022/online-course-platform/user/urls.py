from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.WelcomePage.as_view(), name='welcome'),
    path('student-login/', views.StudentLoginView.as_view(), name='student-login'),
    path('student-register/', views.StudentRegisterView.as_view(), name='student-register'),
]
