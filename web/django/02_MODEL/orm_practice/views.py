from django.shortcuts import render, redirect
from .models import Student


# Retrieve / Read (조회)
def index(request):
    students = Student.objects.all()

    context = {'students': students}

    return render(request, 'orm_practice/index.html', context)


def detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'orm_practice/detail.html', context)


# New (생성)
def new(request):
    return render(request, 'orm_practice/new.html')


def create(request):  # 진짜 저장하는 구간
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.intro = request.GET.get('intro')
    student.save()
    return redirect('index')  # index = /practice/
    # redirect(RAW URL / urls.py의 name): 다시 돌아서 다른데로 가( 이 경우 목록으로 가)