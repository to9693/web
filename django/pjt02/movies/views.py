from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(reqeust):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(reqeust, 'movies/index.html', context)




@login_required
def new(request):

    if request.method == 'POST':
        # 데이터 베이스에 데이터 생성 (ModelForm)
        # 1. 넘어온 데이터를 받기 (title, content)
        movie_form = MovieForm(request.POST)

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # 2. 넘어온 데이터 검증(New)
        if movie_form.is_valid():
            # 3. 데이터베이스에 Article 만들기! (model.form)
            movie = movie_form.save(commit = False)
            # 3-1. user 정보 끼워넣기
            movie.user = request.user
            movie.save()
            # 4. redicrect -> detail
            return redirect('movie:detail', movie.pk)
    else:
        movie_form = MovieForm()
    # 폼을 보여줌
    context = {
        'movie_form' : movie_form,
    }
    return render(request, 'movie/new.html', context)




def detail(request, pk):
    # 1. pk번째 데이터를 가져오기
    movie = Movie.objects.get(pk = pk)
    # 2. context로 넘겨주기
    context = {
        'movie' : movie,
    }
    # 3. render와 함께 html로 넘겨주기
    return render(request, 'movies/detail.html',context)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.method == 'POST':
#         # Article 수정
#         # 1. 넘어온 데이터 받기
#         article_form = ArticleForm(request.POST)
#         # 2. 데이터 검증
#         if article_form.is_valid():
#             # 3. 검증된 데이터로 수정 & 저장
#             article.title = article_form.cleaned_data.get('title')
#             article.content = article_form.cleaned_data.get('content')
#             article.save()
#             # 4. redirect -> detail
#             return redirect('articles:detail', article.pk)
#     else:
#         # Aticle 수정하는 Form 보여주기
#         article_form = ArticleForm(
#             {
#                 'title': article.title,
#                 'content': article.content,
#             }
#         )
#         context = {
#             'article_form' : article_form,
#         }
#         return render(request, 'articles/new.html', context)




@login_required
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    # article의 주인인지 검증
    if request.user != movie.user:
        return redirect('movies:index')

    if request.method == 'POST':
        # Article 수정
        # 1. 넘어온 데이터 받기
        movie_form = MovieForm(request.POST, instance = movie)
        # 2. 데이터 검증
        if movie_form.is_valid():
            # 3. 검증된 데이터로 수정 & 저장
            movie_form.save()
            
            # 4. redirect -> detail
            return redirect('movies:detail', movie.pk)
    else:
        # Aticle 수정하는 Form 보여주기
        movie_form = MovieForm(instance =movie)
    
    context = {
        'movie_form' : movie_form,
    }
    return render(request, 'movies/new.html', context)




@login_required
def delete(reqeust, pk):
    # article의 주인인지 검증
    if request.user != movie.user:
        return redirect('movies:index')

    if request.method =='POST':
        request.movie.delete()
        return redirect('movies:index.html')



 