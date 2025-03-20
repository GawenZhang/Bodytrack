from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from apps.community.models import Post


# Create your views here.
def index(request):
    print("Session Data:", request.session.items())  # 打印 session 内容
    return render(request, 'index.html')


# 用户登录
def login_(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        # 用authenticate判断用户名密码是否正确
        if user:
            login(request, user)
            # 手动存储会话数据
            request.session['username'] = username  # 可以存储额外的信息
            request.session['is_authenticated'] = True  # 自定义存储信息
            return redirect('/')
        else:
            msg = 'Wrong username or password！'
            return render(request, 'login.html', locals())
    return render(request, 'login.html')


# 用户注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if password != password2:
            msg = 'The passwords you entered twice are different！'
            return render(request, 'register.html', locals())
        elif username == '':
            msg = 'Username cannot be empty'
            return render(request, 'register.html', locals())
        cuser = User.objects.create_user(username=username, password=password, email=email)
        cuser.save()
        return redirect('/login/')
    return render(request, 'register.html')


# 登出
# def log_out(request):
#     logout(request)  # 清除用户会话信息
#     return redirect('/')  # 重定向到首页或登录页面

def log_out(request):
    print("Logout view called")  # 调试信息
    auth_logout(request)
    return redirect('/')

@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-created_at')

    # 计算统计数据
    stats = {
        'post_count': posts.count(),
        'comments_count': sum(post.comments_count for post in posts),
        'likes_received': sum(post.likes for post in posts),
        'days_streak': 0,  # 如果没有 Profile，可以硬编码或从其他逻辑计算
    }

    context = {
        'user': user,
        'posts': posts,
        'stats': stats,
    }
    return render(request, 'profile.html', context)


def track(request):
    return render(request, 'track.html')


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('register:profile')  # 包含命名空间
    return redirect('register:profile')  # 包含命名空间