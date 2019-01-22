from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=10,null=False,unique=True)
    aliases = models.CharField(max_length=10,null=True)
    keyword = models.CharField(max_length=20,null=True)
    label = models.CharField(max_length=10,null=True)
    describe = models.CharField(max_length=50,null=True)
    class Meta():
        db_table = 'category'

class Subcategory(models.Model):
     subcategory_name = models.CharField(max_length=10,unique=True,null=False)
     aliases = models.CharField(max_length=10, null=True)
     label = models.CharField(max_length=10,null=True)
     describe = models.CharField(max_length=50, null=True)
     keyword = models.CharField(max_length=20, null=True)
     fid = models.ForeignKey(Category,on_delete=models.CASCADE)
     class Meta():
         db_table = 'subcategory'


        
