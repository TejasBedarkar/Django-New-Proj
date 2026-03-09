from django.shortcuts import render, redirect        #render HTML templates.
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