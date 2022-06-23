from django.conf import settings
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views import View

User = get_user_model()


class WelcomePage(TemplateView):
    template_name = 'user/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome To Digi Academy'
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name)
        u = User.objects.get(id=self.request.user.id)
        if u.is_student:
            return redirect('student:student-dashboard')
        elif u.is_teacher:
            return redirect('teacher:teachers-dashboard')


class StudentLoginView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            u = User.objects.get(id=self.request.user.id)
            if u.is_student:
                return redirect('student:student-dashboard')
        return render(self.request, 'user/student-login.html', {'title': 'DA-Student | Login'})

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user_obj = authenticate(username=email, password=password)
        if user_obj is None:
            messages.error(self.request, "Wrong Credentials. Please Try Again")
            return render(self.request, 'user/student-login.html', {'title': 'DA-Student | Login'})
        elif user_obj.is_student:
            login(self.request, user_obj)
            messages.success(self.request, f"Logged in Successfully as {self.request.user.first_name}")
            return redirect('student:student-dashboard')
        messages.error(self.request, "Permission Error. Not a Student Account")
        return redirect('user:student-login')


class StudentRegisterView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            u = User.objects.get(id=self.request.user.id)
            if u.is_student:
                return redirect('student:student-dashboard')
        return render(self.request, 'user/student-register.html', {'title': 'DA-Student | Register'})

    def post(self, *args, **kwargs):
        print('post')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        first_name = self.request.POST.get('first_name')
        last_name = self.request.POST.get('last_name')
        phone_number = self.request.POST.get('phone_number')
        if User.objects.filter(email=email).exists():
            messages.error(self.request, "Email Already Exists. Please Try Again")
            return redirect('user:student-register')
        else:
            try:
                user_obj = User.objects.create_user(
                    email=email,
                    password=password,
                )
                user_obj.first_name = first_name
                user_obj.last_name = last_name
                user_obj.is_student = True
                user_obj.save()
                messages.success(self.request, "Account created Successfully. Please Login")
                return redirect('user:student-login')
            except Exception as e:
                print(e)
                messages.error(self.request, "Unknown Error..Please Try Again")
                return redirect('user:student-register')


class TeacherLoginView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            u = User.objects.get(id=self.request.user.id)
            if u.is_teacher:
                return redirect('teacher:teachers-dashboard')
        return render(self.request, 'user/teacher-login.html', {'title': 'DA-Teacher | Login'})

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user_obj = authenticate(username=email, password=password)
        if user_obj is None:
            messages.error(self.request, "Wrong Credentials. Please Try Again")
            return redirect('user:teacher-login')
        elif user_obj.is_teacher:
            login(self.request, user_obj)
            messages.success(self.request, f"Logged in successfully as {self.request.user.first_name}")
            return redirect('teacher:teachers-dashboard')
        messages.error(self.request, "Permission Error. Not a Teacher Account")
        return redirect('user:teacher-login')


class TeacherRegisterView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            u = User.objects.get(id=self.request.user.id)
            if u.is_teacher:
                return redirect('teacher:teachers-dashboard')
        return render(self.request, 'user/teacher-register.html', {'title': 'DA-Teacher | Register'})

    def post(self, *args, **kwargs):
        print('post')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        first_name = self.request.POST.get('first_name')
        last_name = self.request.POST.get('last_name')
        phone_number = self.request.POST.get('phone_number')
        if User.objects.filter(email=email).exists():
            messages.error(self.request, "Email Already Exists. Please Try Again")
            return redirect('user:teacher-register')
        else:
            try:
                user_obj = User.objects.create_user(
                    email=email,
                    password=password,
                )
                user_obj.first_name = first_name
                user_obj.last_name = last_name
                user_obj.is_teacher = True
                user_obj.save()
                messages.success(self.request, "Registered Successfully. Please Login to Continue")
                return redirect('user:teacher-login')
            except Exception as e:
                print(e)
                messages.error(self.request, "Unknown Error..Please Try Again")
                return redirect('user:teacher-register')


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return HttpResponseRedirect('/')
