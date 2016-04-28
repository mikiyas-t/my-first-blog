from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# first view - the list of posts ordered y publishing date 
def post_list(request):
    posts = Post.objects.filter(published_Date__lte=timezone.now()).order_by('-published_Date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    
# second view - single post view in detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html',{'post':post})
  
# third view - post new entry
@login_required   
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_Date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})
    
# fourth view - editing existing posts 
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form}) 
    

# fifth view - delete post 
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('blog.views.post_list')


















