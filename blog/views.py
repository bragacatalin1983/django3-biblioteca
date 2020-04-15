from django.shortcuts import render,get_object_or_404
from .models import Blog

def all_blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request,'blog/all_blogs.html',{'blog':blog})

def blog_id(request,nr_id):
    post = get_object_or_404(Blog,pk=nr_id)
    return render(request,'blog/blog_id.html',{'post':post})