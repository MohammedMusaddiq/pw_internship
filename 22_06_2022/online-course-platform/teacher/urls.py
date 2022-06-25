from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.TeacherDashboard.as_view(), name='teachers-dashboard'),
    path('courses/', views.CoursesList.as_view(), name='teachers-courses'),
    path('add-courses/', views.CourseCreate.as_view(), name='create-courses'),
    path('<int:pk>/delete/', views.delete_course, name='delete-course'),
    path('<int:pk>/edit/', views.edit_course, name='edit-course'),
    path('student-list/', views.StudentList.as_view(), name='student-list'),
]
