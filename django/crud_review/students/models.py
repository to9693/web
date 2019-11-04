from django.db import models

# Create your models here.
class Student(models.Model):
     # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 생성된 시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True) # auto_now_add = 생성될때 한번만 , auto_now = 수정될때마다 현재 시간 기록

    #def __str__(self): # 매직 메서드 (특수 목적)
        #return f'{self.id} - {self.name}: {self.age}'
    # str(), print() 호출 시 출력되는 함수

# 1. models.py에 모델 생성
# 2. python manage.py makemigrations 
#     #=> models.py 바탕으로 설계도(migration 파일) 생성
# 3. python manage.py migrate
#     #=> DB(db.sqlite3) 파일에 설계도 적용 (테이블 생성)

# python manage.py shell >> 파이썬 터미널(장고의 설정들이 들어있는 터미널)
# DB에 데이터를 생성하는 방법 3가지
# from articles.models import Article
# 1. article = Article()
#    article.title = '제목'
#    article.content = '내용'
#    article.save()

# 2. article = Article(title='두번째', content='두번째 내용')
#    article.save()

# 3. article = Article.objects.create(title='세번째', content='세번째 내용') 
#    #=> save()할 필요가 없다

# Read
# 1. All- Article.objects.all() # 복수( QuerySet )
# 2. 1개- Article.objects.get(id=)# 단수( Instance ) # unique & not null인 컬럼을 조건으로
#         Article.objects.get(title='세번째')  # title='세번째'인 글이 여러개일 경우 error, 그래서 주로 id값 사용
# 3. 조건- Article.objects.filter(title='세번째') # 복수(QuerySet)
          #-> SQL문의 WHERE
# 4-1. QuerySet + .first(), .last() 
# Article.objects.filter(title='세번째').last() #-> 조건에 해당하는 하나만 반환
# Article.objects.filter(title='안녕') #-> 조건에 해당하는 게 없으면 빈 QuerySet 을 반환
# 
# 4-2. .order_by() : 정렬된 형태로 데이터 가져오기
#      Article.objects.all().order_by('title')  # 오름차순
#      Article.objects.all().order_by('-title') # 내림차순
# 4-3. offset, limit [offset:offset+limit]
#      Article.objects.all()[1:2] #=> [2]번째 인스턴스만 출력

# Update
# 1. 데이터 가져오기 - a = Article.objects.get(id=1)
# 2. 수정할 값 할당하기 - a.title = 'first!' 
# 3. 저장하기 (DB에 반영하기) - a.save()

# Delete
# 1. 데이터 가져오기 - a = Article.objects.get(id=1)
# 2. 삭제하기 (DB에 반영)- a.delete()
# a = Article.objects.get(id=1) #-> 에러 발생


# Student : Comment = 1: N
class Comment(models.Model):
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 생성된 시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True) # auto_now_add = 생성될때 한번만 , auto_now = 수정될때마다 현재 시간 기록
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # CASCADE : 1:N에서 1이 삭제되면 N도 삭제
    # PROTECT : 1을 삭제하려 할 때, N이 있으면 삭제 불가능
    # SET_NULL : 1이 삭제가 되면, N의 컬럼에 NULL로 설정
    # DO_NOTHING : 아무것도 하지 않음

    # 1. 1번 학생(1) 가져오기
    # student = Student.objects.get(pk = 1)

    # 2. 댓글(N) 생성
    # comment = Coment()
    # comment.content = 'First Comment'
    # comment.student = student
    # (comment.student_id = student.pk)
    # comment.save()

    # 3. 댓글(N)로 부터 학생(1) 불러오기
    # comment.student #=> student 인스턴스 자체
    # comment.student.name #=> 학생 이름
    # comment.studnet.age #=> 학생 나이

    # 4. 학생(1)으로부터 댓글(N) 불러오기
    # student.comment_set.all() #=> comment QuerySet