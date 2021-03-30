from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
    # 탈퇴
    path('withdraw/', views.withdraw, name='withdraw'),
    # 개인 프로필
    path('profile/', views.profile, name='profile'),
    # 비밀번호 변경
    path('profile/password/', views.change_password, name='change_password'),
]
