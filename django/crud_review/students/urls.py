from django.urls import path
from . import views

app_name = 'students'

urlpatterns= [
    path('', views.index, name = 'index'), # GET / students/
    path('new/', views.new, name = 'new'), # GET, POST / students/new/
    # path('create/', views.create, name= 'create'), # POST /students/create/
    path('<int:pk>/', views.detail, name = 'detail'), # GET /students/1/
    path('<int:pk>/edit/', views.edit, name = 'edit'), # GET, POST /students/1/edit/
    # path('<int:pk>/update/', views.update, name = 'update'), # POST/ student/1/update/
    path('<int:pk>/delete/', views.delete, name = 'delete'), # POST/ sutdnet/1/delete/
]

# URL Name -> 각각의 path에 적용
# path('주소/', views.함수, name = '이름')
# {% %} django templates language 문법을 사용
# {% url '이름' %}
# {% url 'new' %} # -> /student/new/
# [장점]
# 1. 주소의 변경이 필요할 때, urls.py에서만 수정해주면 됨
# 2. 마지막 '/'를 빼먹는 실수를 차단할 수 있음

# App Name -> 특정 app의 urls.py에 적용
# {% url 'students:index' %}
# {% url '앱이름:path_name' %}

# RESTful
# 1. 자원(Resource) - URL
# 2. 행위(Verb) - HTTP Method(GET, POST, ...)
# 3. 표현(Representations) - 자원 + 행위

# Django는 PUT/PATCh/DELETE 불가능. 따라서...
# GET  /studnets/2/edit/ #=> 수정 페이지 보여줌
# POST /students/2/edit/ #=> 수정 작업 진행