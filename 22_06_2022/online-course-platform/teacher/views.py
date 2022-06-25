from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Course
from student.models import CourseRegistration


class TeacherDashboard(TemplateView):
    template_name = 'teacher/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"DA | {self.request.user.first_name}"
        context['navbar'] = "teacher-dashboard"
        return context


class CoursesList(ListView):
    template_name = 'teacher/courses.html'
    model = Course

    def get_queryset(self):
        return Course.objects.filter(instructor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"DA | {self.request.user.first_name}"
        context['navbar'] = "teacher-courses"
        return context


class CourseCreate(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'teacher/add-courses.html',
                      {'title': f'DA | {self.request.user.first_name}', 'navbar': 'teacher-courses'})

    def post(self, *args, **kwargs):
        course_title = self.request.POST.get('course-title')
        course_description = self.request.POST.get('course-description')
        content = self.request.POST.get('content')
        try:
            c = Course.objects.create(
                instructor=self.request.user,
                course_name=course_title,
                course_description=course_description,
                content=content,
            ).save()
            messages.success(self.request, "Course created successfully")
            return redirect('teacher:teachers-courses')
        except Exception as e:
            messages.error(self.request, "Something went wrong. Try again")
            print(e)
            return redirect('teacher:create-courses')


def delete_course(request, pk):
    obj = Course.objects.get(id=pk)
    obj.delete()
    return redirect('teacher:teachers-courses')


def edit_course(request, pk):
    c = Course.objects.get(id=pk)
    if request.method == 'POST':
        cname = request.POST.get('course-title')
        desc = request.POST.get('course-description')
        content = request.POST.get('content')
        c.instructor = request.user
        c.course_name = cname
        c.course_description = desc
        c.content = content
        c.save()
        messages.success(request, "Updated the Selected Course")
        return redirect('teacher:teachers-courses')
    context = {
        'course': c,
        'title': f'DA | {request.user.first_name}',
        'navbar': 'teacher-courses'
    }
    return render(request, 'teacher/edit-course.html', context)


class StudentList(ListView):
    template_name = 'teacher/students.html'
    paginate_by = 8

    def get_queryset(self):
        print(CourseRegistration.objects.filter(course__instructor_id=self.request.user.id))
        return CourseRegistration.objects.filter(course__instructor_id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"DA | {self.request.user.first_name}"
        context['navbar'] = "teacher-students"
        return context
