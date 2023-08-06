from django.shortcuts import render,redirect
from bapp.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import Category_form,Blog_form

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

# for delete 

def delete(request,id):
    category=Category.objects.get(pk=id)
    category.delete()
    return redirect('category')





def edit(request,id):
    if request.method == 'POST':
        get_object=Category.objects.get(id=id)
        forms=Category_form(request.POST)
        if forms.is_valid():
            category_name=forms.cleaned_data['category_name']
            get_object.category_name=category_name
            get_object.save()
            return redirect('category')
        
    forms=Category_form()
    context={
        'id':id,
        'forms':forms,
    }
    return render(request,'dashboard/edit.html',context)