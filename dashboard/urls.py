from . import views
from django.urls import path


urlpatterns = [
   
path('',views.dashboard,name='dashboard'),
path('category/',views.category,name='category'),
path('category/add',views.add,name='add'),
path('category/delete/<int:id>',views.delete,name='delete'),
  
]