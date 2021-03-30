# 데이터 보내기, 받기
from django.shortcuts import render, redirect, get_object_or_404
# POST, GET
from django.views.decorators.http import require_safe, require_POST, require_http_methods
# login 했는지확인: not login일 경우에 무조건 'accounts/login/'으로 redirect한다
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 비밀번호 변경 해쉬
from django.contrib.auth import update_session_auth_hash


user = get_user_model()

# 가입
@require_http_methods(['GET','POST'])
def signup(request):
    # login 한 사용자라면 목록으로 그냥 보내기
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = { 'form': form }
    return render(request, 'accounts/signup.html', context)


# 로그인
# next: 로그인 안되어있으면 login.url으로 보냄(GET) => else(GET)
# => html의 form(POST) => login request.POST
# login_required: login 했는지확인, not login일 경우에 무조건 'accounts/login/'으로 next를 가지고 redirect한다
# ex) create위에 있는 @login_required에서 보내졌다면 ?next=articles/create
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')
            return redirect(next_url or 'articles:index')
    else:
        form = AuthenticationForm()
    context = { 'form': form,}
    return render(request, 'accounts/login.html', context)


# 로그아웃
@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


# 탈퇴
@login_required
@require_POST  # 혹시나 생길 오류 막으려구, POST로 안 해놓으면 접근이 너무 쉬워진다.(url에 심심해서 delete쓰면 탈퇴당함...;;)
def withdraw(request):
    request.user.delete()  # 바껴도 되는데 없으면 안된다. 데이터베이스에서 기록 제거
    auth_logout(request)  # 인터넷 cookie 회수, session 테이블에서 레코드 삭제.
    return redirect('articles:index')

# 개인 프로필
@login_required
def profile(request):
    user = request.user
    context = { 'user': user }
    return render(request, 'accounts/profile.html', context)


# 비밀번호 변경
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()  # save먼저 해야 로그인 유지
            update_session_auth_hash(request, form.user)  # 해시 업데이트
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = { 'form': form }
    return render(request, 'accounts/change_password.html', context)

# # 개인 프로필
# @login_required
# # /accounts/profile/<neo>/
# def profile(request, username):  # 프로필 페이지
#     user = get_object_or_404(User, username=username)  
#     context = {'user_profile': user, }
#     """
#     request.user => /profile/<username>/ 으로 요청을 보낸 사람
#     user => /profile/<username>/ 에서 username 에 해당하는 사람
#     둘이 같을 때, Update 로직(form, valid 등..)이 실행됨 / 그게 아니라면 단순 조회 페이지
#     """
#     if request.user == user:
#         if request.method == 'POST':
#             form = CustomUserChangeForm(request.POST, instance=user)
#             if form.is_valid():
#                 user = form.save()
#                 return redirect('accounts:profile', username=user.username)
#         else:
#             form = CustomUserChangeForm(instance=user)
#         context['form'] = form 
#     return render(request, 'accounts/profile.html', context)