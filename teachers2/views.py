from django.shortcuts import render
from .models import Teacher

# Create your views here.

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teacher_index.html', context)

def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher_detail.html', context)