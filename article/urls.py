from django.urls import path

from article import views

urlpatterns = [
    path('add-article/',views.add_article,name='add-article'),
    # path('select_category/',views.select_category,name='select_category'),
    path('index/',views.index,name='index'),
    path('del_article/<int:id>/',views.del_article,name='del_article'),
    path('update_article/<int:id>/',views.update_article,name='update_article'),

]