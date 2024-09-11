from django.shortcuts import render
from .models import Blogs
# Create your views here.
def all_blogs(request):

	blogs = Blogs.objects.order_by("-date")[:5]
#instead of showing all the blogs we can do order.by - date most current will show up 
	return render(request,"blog/all_blogs.html" , {'blogs': blogs})



def detail(request ,blog_id):
	return render(request,'blog/detail.html',{'id':blog_id})


