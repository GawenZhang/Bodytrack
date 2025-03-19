from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse

from .models import Post, Category, Topic, Event, Follow, Comment, Tag
from django.core.paginator import Paginator

def community_home(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    topics = Topic.objects.all()
    events = Event.objects.order_by('date')[:3]
    recommended_users = User.objects.exclude(id=request.user.id)[:3] if request.user.is_authenticated else User.objects.all()[:3]

    stats = {
        'members': User.objects.count(),
        'active_today': Post.objects.filter(created_at__date__gte='2025-03-18').count(),
        'total_posts': Post.objects.count(),
    }

    context = {
        'posts': page_obj,
        'categories': categories,
        'topics': topics,
        'events': events,
        'recommended_users': recommended_users,
        'stats': stats,
    }
    return render(request, 'community.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views += 1  # 增加浏览量
    post.save(update_fields=['views'])

    comments = post.comments.all().order_by('-created_at')
    paginator = Paginator(comments, 5)  # 每页5条评论
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            return redirect(f'/post/{post.id}/')  # 直接跳转到帖子详情页面，去掉了反向解析

    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)[:3]

    context = {
        'post': post,
        'comments': page_obj,
        'related_posts': related_posts,
    }
    return render(request, 'post_detail.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Tag

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_name = request.POST.get('category')  # 获取类别名称
        image = request.FILES.get('image')
        tags_input = request.POST.get('tags', '')

        # 处理分类（获取或创建 Category 实例）
        category, _ = Category.objects.get_or_create(name=category_name)

        # 创建帖子
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            category=category,  # 传入 Category 实例
            image=image
        )

        # 处理标签（多个标签逗号分隔）
        if tags_input:
            tag_names = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

        # 确保跳转到正确的 URL
        return redirect(f'/community/post/{post.id}/')

    # 获取所有类别供前端选择（假设 create_post.html 需要下拉选择框）
    categories = Category.objects.all()

    return render(request, 'create_post.html', {'categories': categories})




@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    if not created:
        follow.delete()
        return JsonResponse({'status': 'unfollowed'})
    return JsonResponse({'status': 'followed'})