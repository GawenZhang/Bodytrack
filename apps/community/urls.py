from django.urls import path
from . import views  # 使用相对导入，更简洁

app_name = 'community'  # 设置命名空间

urlpatterns = [
    path('', views.community_home),
    path('create_post/', views.create_post),
    path('post/<int:post_id>/', views.post_detail),
    path('like/<int:post_id>/', views.like_post),
    path('follow/<int:user_id>/', views.follow_user),
]