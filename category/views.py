from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from category.models import Category, Subcategory


def add_category(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        return render(request,'category.html',{'categorys':categorys})
    if request.method == 'POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        fid = int(request.POST.get('fid'))
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        if fid == 0:
            Category.objects.create(category_name=name,aliases=alias,keyword=keywords,describe=describe)

            return HttpResponseRedirect(reverse('category:add_category'))
        else:
            Subcategory.objects.create(subcategory_name=name,aliases=alias,keyword=keywords,describe=describe,fid_id=fid)
            return HttpResponseRedirect(reverse('category:add_category'))


def del_category(request,id):
    if request.method == 'GET':
        Category.objects.filter(id=id).first().delete()
        return HttpResponseRedirect(reverse('category:add_category'))

def update_category(request,id):
    if request.method == 'GET':
        category = Category.objects.filter(id=id).first()
        return render(request,'update-category.html',{'category':category})
    if request.method == 'POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        Category.objects.filter(id=id).update(category_name=name,aliases=alias)
        return HttpResponseRedirect(reverse('category:add_category'))
