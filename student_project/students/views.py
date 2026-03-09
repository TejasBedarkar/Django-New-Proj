from django.shortcuts import render          #render HTML templates.
from .models import Student                  #to query Student table

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})