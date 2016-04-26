from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


# first view - the list of posts ordered y publishing date 
def post_list(request):
    posts = Post.objects.filter(published_Date__lte=timezone.now()).order_by('-published_Date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html',{'post':post})