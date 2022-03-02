from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import post,Category
from .forms import postform , editform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def home(request):
    #eturn render(request,'home.html')
def LikeView(request,pk):
    pos = get_object_or_404(post, id = request.POST.get('post_id'))
    pos.likes.add(request.user)
    return HttpResponceRedirect(reverse('article-details', args=[str(pk)]))

class HomeView(ListView):
    model = post
    template_name = 'home.html'
    ordering = ['-post_date']
class inputview(DetailView):
    model = post
    template_name ='input.html'
class addview(CreateView):
    model = post
    form_class = postform
    template_name  = 'add_post.html'
class addcategoryview(CreateView):
    model = Category
    #form_class = postform
    template_name  = 'add_category.html'
    fields = '__all__'
class updateview(UpdateView):
    model = post
    form_class = editform
    template_name = 'update_post.html'
    #fields=['title','author','body']
class deleteview(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
