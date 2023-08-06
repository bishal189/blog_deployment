from django.shortcuts import render,redirect
from bapp.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import Category_form

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    total_post=Blog.objects.all().count()
    total_category=Category.objects.all().count()
    context={
        'total_post':total_post,
        'total_category':total_category
    }
    return render(request,'dashboard/dashboard.html',context)




def category(request):
    return render(request,'dashboard/category.html')



# add category
def add(request):
    if request.method=='POST':
        forms=Category_form(request.POST)
        if forms.is_valid():

            forms.save()
            return redirect('category')

    else:        
        forms=Category_form()
    context={
        'forms':forms
    }
    return render(request,'dashboard/add.html',context)



def delete(request,id):
    category=Category.objects.get(pk=id)
    category.delete()
    return redirect('category')