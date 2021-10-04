from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
                                )
from .models import post
from django.urls import reverse_lazy
from django.contrib.auth.models import User

'''@login_required()
def home(request):
    return render(request,'home/home.html')
'''
#--------------------------------------------------
class UserpostListView(LoginRequiredMixin,ListView):
    model=post
    template_name='home/user_post.html'
    context_object_name='posts'
    
    def get_queryset(self):
       # print(self.kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        return post.objects.filter(author=user).order_by('-date_posted')
#--------------------------------------------------- 
class postDetailView(LoginRequiredMixin,DetailView):
    model=post
    template_name='home/post_datail.html'
    context_object_name='post'
   

#--------------------------------------------------
class postCreateView(LoginRequiredMixin,CreateView):
    model=post
    fields=['content']
    #success_url=f'/post/{object.id}'
  
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
#---------------------------------------------------
class postUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['content']
  
    def form_valid(self, form):#save model
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
#-----------------------------------------------------
class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url=reverse_lazy('home')
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
#----------------------------------------------------
class CreateListPost(postCreateView):
    template_name='home/home.html'
    success_url=reverse_lazy('home')
    def get_context_data(self, **kwargs): #send dic data
        temp=post.objects.order_by('-date_posted')
        content=super().get_context_data(**kwargs)
        content['posts']=temp[0:10]
        #print(content)
        return content
 