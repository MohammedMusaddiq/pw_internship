from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Course, Content


class TeacherDashboard(TemplateView):
    template_name = 'teacher/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"DA | {self.request.user}"
        context['navbar'] = "teacher-dashboard"
        return context


class CoursesList(ListView):
    template_name = 'teacher/courses.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"DA | {self.request.user}"
        context['navbar'] = "teacher-courses"
        return context
