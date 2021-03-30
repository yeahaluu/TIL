from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # Create(생성)
    path('create/', views.create, name='create'),

    # Read(읽기)
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    # Update(수정)
    path('<int:article_pk>/update/', views.update, name='update'),

    # delete(삭제)
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    
    # 댓글 생성
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),

    # 댓글 삭제
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
