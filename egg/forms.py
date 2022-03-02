from django import forms
from .models import post,Category

choices = Category.objects.all().values_list('name','name')
category_list = []
for i in choices:
    category_list.append(i)
class postform(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','author','category','body')
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'please enter title'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=category_list,attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'please enter your text'}),
        }

class editform(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','author','body')
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'please enter title'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'please enter your text'}),
        }
