from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    # 로그인 유무 판별 & 로그인 된 경우 redirect
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        # 실제 회원 생성
        # 1. 넘어온 데이터를 Form Class에 입력하기
        form = UserCreationForm(request.POST)

        # 2. 유효한 값인지 검증
        if form.is_valid():
            # 3. 회원 생성
            user = form.save()
            # 3-1. 로그인
            auth_login(request, user)
            # 4. redirect -> 메인페이지(articles index)
            return redirect('movies:index')


    else:
        # 회원 가입 양식 보여줌
        form = UserCreationForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)




def login(request):
    if request.user.is_authenticated:
    
        return redirect('moives:index')
    if request.method == 'POST':
        # 로그인
        # 1. POST 요청으로 넘어온 데이터를 Form에 입력
        form = AuthenticationForm(request, request.POST)
        # 2. 검증
        if form.is_valid():
            # 3. 로그인 수행
            auth_login(request, form.get_user())
            # 4. redirect -> 메인 페이지 (articles index)
            return redirect('moives:index')
            # 4-1. next 값 가져오기
            next = request.GET.get('next')
            return redirect(next or 'movies:index')
    else:
        # 로그인 창 보여줌
        form = AuthenticationForm()

    context= {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)





def logout(request):
    if request.method == 'POST':
        # 로그아웃 수행
        auth_logout(request)
        return redirect('movies:index')


# Sign up vs. Login
# 1. Signup
# User를 Create

# 2. Login
# Session에서 User 정보를 Create

# 3. Logout
# Session에서 User 정보를 Delete

# Session이란?
# Django가 브라우저의 정보를 임시로 들고 있으면서
# 지금 이 페이지를 보는 User가 누구인지
# 서버쪽에서 정보를 들고 있는 것.