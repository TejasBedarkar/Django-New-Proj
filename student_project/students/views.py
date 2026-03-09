from django.shortcuts import render, redirect, get_object_or_404        #render HTML templates.
from .models import Student                  #to query Student table
from .forms import StudentForm

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