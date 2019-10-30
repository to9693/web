from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all().order_by('-id') #=> QuerySet ~= list()

    context = {
        'students': students,
    }
    return render(request, 'students/index.html', context)

def new(request):
    return render(request, 'students/new.html')

def create(request): # POST 요청을 받음
    # 넘어온 데이터 받기
    # 이유 2번 - GET(URL), POST(http body)
    name = request.GET.get('name')
    age = request.GET.get('age')

    student = Student.objects.create(name=name, age = age)

    return render(request, f'/students/{student.pk}/')