from django.shortcuts import render, redirect, get_object_or_404        #render HTML templates.
from .models import Student                  #to query Student table
from .forms import StudentForm
#django ka inbuild regis form
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        
    else:
        form = StudentForm()
        
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)              #Fetch student whose id matches
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)    #Update existing record instead of creating new one
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:           #login siccessful
            login(request, user)       #create session for user
            return redirect('student_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')