from . import views
from django.urls import path


urlpatterns = [
   
path('',views.dashboard,name='dashboard'),
path('category/',views.category,name='category'),
path('category/add',views.add,name='add'),
path('category/delete/<int:id>',views.delete,name='delete'),
path('category/edit/<int:id>',views.edit,name='edit'),
path('add_post/',views.add_post,name='add_post'),
path('blogs/',views.blog,name='blog'),
path('blogs/post_delete/<int:id>',views.post_delete,name='post_delete'),
path('blogs/post_edit/<int:id>',views.post_edit,name='post_edit'),
  
]