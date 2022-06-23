from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentDashboard.as_view(), name='student-dashboard'),
]
