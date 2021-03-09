from django.urls import path, include
# from . import views  # 같은 패키지 내부에서 들고올 때 .


urlpatterns = [
    # path('test/', views.test)  # 포워딩
    path('articles/', include('articles.urls')),
]
