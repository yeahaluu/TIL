from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ContactForm, ArticleForm


"""
new와 create를 한번에 담당
1. 사용자가 /crud/contact/ 로 접속 => GET/curd/contact/
2. 사용자가 HTML > form 에서 데이터 제출 => POST/crud/contact/
3. view 함수에서 contact로 redirect 시킴 => GET/crud/contact/
form 태그에서 버튼 누르는 것(post) 제외한 모든 것은 get!
"""
def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'articles/contact.html', context)
    elif request.method =='POST':
        contact_form = ContactForm(request.POST)
        print(contact_form.is_valid())
        print(contact_form.errors)
        return redirect('contact')

def new(request):
    if request.method =='GET':
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'articles/new.html', context)
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_form = form.save()
        
            return redirect('detail', article_pk=article.pk)


def index(request):
    articles = Article.pbjects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html',context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method =='GET':
        # 기존 게시글 내용을 포함한 HTML을 만들기 위해 instance 추가
        form = ArticleForm(instance=article)
        context = {'form': form}
        return render(request, 'articles/new.html', context)

    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_form = form.save()
            return redirect('detail', article_pk=article.pk)


def delete(request, article_pk):
    return recirect()