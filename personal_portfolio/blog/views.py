from django.shortcuts import render, get_object_or_404
# get object is for finding a object if it is not present then it gives 404 page
from .models import Blogs
# Create your views here.
def all_blogs(request):

	blogs = Blogs.objects.order_by("-date")
#instead of showing all the blogs we can do order.by - date most current will show up 
	return render(request,"blog/all_blogs.html" , {'blogs': blogs})



def detail(request ,blog_id):
	blog = get_object_or_404(Blogs,pk = blog_id)
	return render(request,'blog/detail.html',{'blog':blog})


