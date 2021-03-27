from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


# New (생성)
## HTML 제공
def new(request):
    return render(request, 'orm_practice/new.html')


def create(request):  # 진짜 저장하는 구간
    if request.method =='POST':
        student = Student()
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.intro = request.POST.get('intro')
        student.save()
        return redirect('detail', pk=student.pk)  # 이 경우 목록으로 가 , index = /practice/
    # return redirect('detail', student.name=pk)  # 이 경우 내가 쓴 글로 가
    # redirect(RAW URL / urls.py의 name): 다시 돌아서 다른데로 가
    return redirect('edit')


# Retrieve / Read (조회)
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'orm_practice/index.html', context)


def detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student }
    return render(request, 'orm_practice/detail.html', context)



# Update
## 수정용 HTML 제공
def edit(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student}
    return render(request, 'orm_practice/edit.html', context)

# 실제 수정
def update(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.intro = request.POST.get('intro')
        student.save()
        return redirect('detail', pk=student.pk)
    return redirect('edit', pk=pk)



#Delete
def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('index')  # detail로 보낼 수 없다.
    return redirect('detail', pk=pk)