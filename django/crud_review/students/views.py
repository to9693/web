from django.shortcuts import render, redirect
from .models import Student, Comment

# Create your views here.
def index(request):
    # 1. 모든 student를 DB에서 가져오기
    
    students = Student.objects.all().order_by('-id') #=> QuerySet ~= list()

    # 2. context에 저장
    context = {
        'students': students,
    }

    # 3. render 하면서 context 넘겨주기
    return render(request, 'students/index.html', context)

def new(request):
    if request.method == 'POST':  #=> 'GET', 'POST'
        # 넘어온 데이터 받기
        # 이유 2번 - GET(URL), POST(http body)
        # 1. POST 요청으로 넘어온 데이터 가져오기 new.html에서 넘어옴 
        name = request.POST.get('name')
        age = request.POST.get('age')

        # 2. DB에 저장!

        # 다른 방법student = Student.objects.create(name=name, age = age)
        student = Student(name= name, age =age)
        student.save()

        # 3.생성된 학생의 상세 정보를 보는 페이지로 이동(Detail))
        return redirect('students:detail', student.pk)

            # students를 생성함 
    else:
        # new page를 보여주면 됨 (def new)
        return render(request, 'students/new.html')

    

# def create(request): # POST 요청을 받음
#     # 넘어온 데이터 받기
#     # 이유 2번 - GET(URL), POST(http body)
#     # 1. POST 요청으로 넘어온 데이터 가져오기 new.html에서 넘어옴 
#     name = request.POST.get('name')
#     age = request.POST.get('age')

#     # 2. DB에 저장!

#     # 다른 방법student = Student.objects.create(name=name, age = age)
#     student = Student(name= name, age =age)
#     student.save()

#     # 3.생성된 학생의 상세 정보를 보는 페이지로 이동(Detail))
#     return redirect('students:detail', student.pk)

def detail(request, pk):
    # 1. pk 에 해당하는 student를 DB에서 가져오기
    student = Student.objects.get(pk=pk) # => student 인스턴스

    # 2. context에 저장
    context = {
        'student' : student,
    }
    # 3. rnder 하면서 context 넘겨주기
    return render(request, 'students/detail.html', context)

def edit(request, pk):
    student= Student.objects.get(pk=pk)
    if request.method == 'POST':
        # student를 수정 (def update)
        
        student = Student.objects.get(pk=pk)

        # 2. POST 요청을 통해 넘어온 데이터 가져오기
        name = request.POST.get('name')
        age = request.POST.get('age')

        # 3. student 인스턴스의 정보를 변경
        student.name = name
        student.age = age
        student.save() 

        return redirect('students:detail', student.pk )
    else:
        # 수정하는 페이지를 보여줌 (def edit) # 1. pk에 해당하는 학생 DB에서 가져오기
        

        context = {
            'student' : student,
        }
        return render(request, 'students/edit.html', context)
   

# POST 요청만을 받음 -> redirect()
# def update(request, pk):
    # # 1. pk에 해당하는 student를 DB에서 가져오기
    # student = Student.objects.get(pk = pk)

    # # 2. POST 요청을 통해 넘어온 데이터 가져오기
    # name = request.POST.get('name')
    # age = reqeust.POST.get('age')

    # # 3. student 인스턴스의 정보를 변경 & DB에 반영 -> .save()
    # student.name = name
    # student.age = age
    # student.save()

    # # 4. student 상세 페이지로 이동(Detail)
    # return redirect('student:detail', student.pk)

   

# POST 요청만을 받음 -> redirect()
def delete(request, pk):
    if request.method =='POST':

        # 1. pk에 해당하는 학생을 DB에서 가져옴
        student = Student.objects.get(pk = pk) 
 
        # 2. student 삭제(DB에서 삭제하기))
        student.delete()

        # 3. index  페이지로 이동
        return redirect('students:index')


# POST 요청을 받음 => redirect
def comments_new(request, student_pk):
    # 1. request에서 데이터 가져오기
    content = request.POST.get('content')
    
    # 2. Comment 생성
    comment = Comment()
    comment.content = content
    comment.student_id = student_pk
    comment.save()

    # 3. student 상세 페이지로 redirect
    return redirect('students:detail', student_pk)

# POST 요청을 받음
def comments_delete(reqeust, student_pk ,pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('studentsLdetail', student_pk)

def comments_edit(request, student_pk, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'PSOT':
        # POST
        # 1. POST로 넘어온 데이터 가져오기
        content = request.POST.get('content')

        # 2. comment에 바꿔 넣기 & 저장
        comment.content = content
        comment.save()
        return redirect('students:detail', student_pk)

    else:
        # GET
        context = {
            'comment' :comment,
        }
        return render(request, 'students/comments_edit.html', context)
