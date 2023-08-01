from django.shortcuts import render
from .models import Blogs , comments 
# Create your views here.


def show_Blog(request) : 
    data = Blogs.objects.all()
    content = {
        'info' : data , 

    }

    return render(request , 'blog.html' , content )


def detail_blog(request , id ) : 
    recent_post = Blogs.objects.all().order_by("-time")
    post_now = Blogs.objects.get(id = id )
    data_comments = comments.objects.all().filter(blog = post_now )
    content = {
        'info' : Blogs.objects.get(id = id ) ,
        'recent' : recent_post , 
        'comments' : data_comments , 

    }
    return render(request , 'blog-details.html' , content )
