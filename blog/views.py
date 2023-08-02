
from django.shortcuts import redirect,render
from bapp.models import Category ,Blog

def home(request):
    category=Category.objects.all()
    featured=Blog.objects.filter(is_featured=True,status='Published').order_by('created_at')
    not_featured=Blog.objects.filter(is_featured=False,status='Published')
    
    context={
        'category':category,
        'featured':featured,
        'not_featured':not_featured
    }


    return render(request,'home/home.html',context)