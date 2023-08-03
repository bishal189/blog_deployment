from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from .models import Category,Blog

def post_by_category(request,category_id):
    # fetching the blog post based on category_id or category
    posts=Blog.objects.filter(status='Published',category_id=category_id)
    try:
       category_name=Category.objects.get(pk=category_id)

    except:
        return redirect('home')   
    

    context={
        'post':posts,
        'category_name':category_name
    }
    return render(request,'home/category.html',context)
   
   
    
    
