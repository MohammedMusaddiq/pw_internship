from django.conf import settings
from django.contrib.auth import login, authenticate, get_user_model
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


class StudentLoginView(View):
    def get(self, *args, **kwargs):
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
            return redirect('user:welcome')
        messages.error(self.request, "Permission Error. Not a Student Account")
        return redirect('user:student-login')


class StudentRegisterView(View):
    def get(self, *args, **kwargs):
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
                return redirect('user:welcome')
            except Exception as e:
                print(e)
                messages.error(self.request, "Unknown Error..Please Try Again")
                return redirect('user:student-register')
