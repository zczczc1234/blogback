from django.db import models

from category.models import Category, Subcategory


class Article(models.Model):
    title = models.CharField(max_length=20,null=False)
    content = models.TextField(null=False)
    keyword = models.CharField(max_length=20,null=True)
    describe = models.CharField(max_length=80,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20,null=False)
    cid = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    sid = models.ForeignKey(Subcategory,null=True,on_delete=models.SET_NULL)
    class Meta():
        db_table = 'article'

