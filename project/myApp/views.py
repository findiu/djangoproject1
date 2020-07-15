from django.shortcuts import render

# Create your views here.
#视图就是函数
from django.http import HttpResponse
def index(request):
    return HttpResponse("hell world django")
def sz(request):
    return HttpResponse("sz")
from .models import Grades,Students
def grades(request):
    gradesList = Grades.objects.all()
    return render(request,'myApp/grades.html',{"grades":gradesList})
def students(request):
    studentsList=Students.objects.all()
    return render(request,'myApp/students.html',{"students":studentsList})

