from django.shortcuts import render
from . models import Blogs

# Create your views here.
def blog(request):
    posts=Blogs.objects.all()
    return render(request,'blog/blog.html',{'posts':posts})
