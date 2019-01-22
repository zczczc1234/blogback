from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=10,unique=True,null=False)
    password = models.CharField(max_length=150,null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table = 'admin'

