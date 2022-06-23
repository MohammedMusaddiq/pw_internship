from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.TeacherDashboard.as_view(), name='teachers-dashboard'),
    path('courses/', views.CoursesList.as_view(), name='teachers-courses'),
]
