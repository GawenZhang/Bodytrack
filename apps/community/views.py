from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

# 帖子列表（主页）
def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'posts': posts})

# 帖子详情
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post_detail', post_id=post_id)
    return render(request, 'post_detail.html', {'post': post})

# 创建帖子（需要登录）
@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_list')
    return render(request, 'create_post.html')