from django.shortcuts import render
from django.views.generic import TemplateView


class StudentDashboard(TemplateView):
    template_name = 'student/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"DA | {self.request.user}"
        context['navbar'] = "student-dashboard"
        return context
