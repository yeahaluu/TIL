from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create(생성)
@login_required
@require_http_methods(['GET','POST'])
def create(request):
    user = request.user
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = { 'form':form }
    return render(request, 'articles/create.html', context)


# Read(읽기)
def index(request):  # 목록
    articles = Article.objects.all()
    context = { 'articles': articles }
    return render(request, 'articles/index.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 댓글 작성 form
    comment_form = CommentForm()
    # 댓글 목록
    comments = article.comment_set.all()
    context = { 
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        }
    return render(request, 'articles/detail.html', context)


# Updatd(수정)
@require_http_methods(['GET','POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # new와 다르게, 특정 article에 대한 내용을 request.POST로 덮어 쓰기.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 기존 게시글 내용을 포함한 HTML 만들기 위해 instance 추가
        form = ArticleForm(instance=article)
    context = { 'form': form }
    return render(request, 'articles/update.html', context)


# Delete(삭제)
@login_required
# @require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


# 댓글 생성
@require_POST
def create_comment(request, article_pk):
    if request.user.is_authenticated:
        user = request.user
        article = get_object_or_404(Article, pk=article_pk)
        comment_form=CommentForm(request.POST)
        comments = article.comment_set.all()
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = user
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form':comment_form,
            'article': article,
            'comments':comments,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

# 댓글 삭제
@login_required
@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)







# @require_http_methods(['GET','POST'])
# def create(request):
#     if request.method == 'GET':
#         form = ArticleForm()
#         context = { 'form': form }
#         return render(request, 'articles/create.html')
#     elif request.method == 'POST':
#         #form에 요청 데이터를 입력
#         form = ArticleForm(request.POST)
#         # form을 통해 유효성 검사
#         if form.is_valid():
#             # 유효하다면, 저장
#             article = form.save()
#             # 저장한 article의 상세보기 페이지로 redirect
#             return redirect('articles:detail', article_pk=article.pk)
#         else:
#             # 유효하지 않으면, 기존의 잘못된 data담은 form을 담고
#             cotext = { 'form':form }
#             # html실어서 전송
#             return render(request, 'articles/create.html', context)