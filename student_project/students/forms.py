from django import forms
from .models import Student       #connect to Student model

class StudentForm(forms.ModelForm):   #here we telling django that we want to create a form based on the Student model

    class Meta:                         #define form configuration
        model = Student                  #form will use Student table field
        fields = ['name', 'email', 'course', 'age']