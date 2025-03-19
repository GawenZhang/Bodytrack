from django.urls import path
from . import views  # 使用相对导入，更简洁

app_name = 'community'  # 设置命名空间

urlpatterns = [
    # path('', views.community, name='community'),
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # 添加或确认这一行
    # path('create/', views.create_post, name='create_post'),
    # path('', views.community_home, name='community_home'),
    # path('create_post/', views.create_post, name='create_post'),
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('like/<int:post_id>/', views.like_post, name='like_post'),
    # path('follow/<int:user_id>/', views.follow_user, name='follow_user'),

    path('', views.community_home),
    path('create_post/', views.create_post),
    path('post/<int:post_id>/', views.post_detail),
    path('like/<int:post_id>/', views.like_post),
    path('follow/<int:user_id>/', views.follow_user),

]