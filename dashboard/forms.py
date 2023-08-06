from django import forms
from bapp.models import Category,Blog

class Category_form(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'



class Blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'