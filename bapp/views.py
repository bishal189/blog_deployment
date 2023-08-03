from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Category,Blog
from django.db.models import Q

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
   
   
    


    # for single post



def single_post(request,slug):
    single_post=get_object_or_404(Blog,slug=slug)
    context={
        'single_post':single_post
    }
    return render(request,'home/single_post.html',context)
    
    



def search(request):
    keyword=request.GET['search']
    blogs=Blog.objects.filter(Q(title__icontains=keyword)|Q( descriptions__icontains=keyword)|Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'home/search.html',context)