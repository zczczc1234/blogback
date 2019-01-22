from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from article.models import Article
from category.models import Subcategory, Category


def index(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        articles = Article.objects.all()
        pg = Paginator(articles,3)
        articles = pg.page(page)
    return render(request,'article.html',{'articles':articles})

# def select_category(request):
#     if request.method == 'GET':
#         subcategorys = Subcategory.objects.all()
#         return render(request,'add-article.html',{'subcategorys':subcategorys})

def add_article(request):
    if request.method == 'GET':
        subcategorys = Subcategory.objects.all()
        return render(request, 'add-article.html', {'subcategorys': subcategorys})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        category_id = request.POST.get('category_id')
        print(category_id)
        if not title:
            info = '未输入标题'
            return HttpResponseRedirect(reverse('article:add-article'))
        elif not content:
            info = '未输入文章内容'
            return HttpResponseRedirect(reverse('article:add-article'))
        else:
            subcategory = Subcategory.objects.filter(id=category_id).first()
            category_id = subcategory.fid_id
            category = Category.objects.filter(id=category_id).first()
            category_name = category.category_name
            Article.objects.create(title=title,content=content,keyword=keywords,describe=describe,category=category_name)
            return HttpResponseRedirect(reverse('article:index'))

def del_article(request,id):
    if request.method == 'GET':
        Article.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('article:index'))


def update_article(request,id):
    if request.method == 'GET':
        article = Article.objects.filter(id=id).first()
        print(article)
        return render(request,'update-article.html',{'article':article})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.filter(id=id).update(title=title,content=content)
        return HttpResponseRedirect(reverse('article:index'))