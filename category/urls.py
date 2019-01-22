from django.urls import path

from category import views

urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('del_category/<int:id>/',views.del_category,name='del_category'),

]