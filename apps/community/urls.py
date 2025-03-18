from django.urls import path
from . import views  # 使用相对导入，更简洁

app_name = 'community'  # 设置命名空间

urlpatterns = [
    path('', views.community, name='community'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # 添加或确认这一行
    path('create/', views.create_post, name='create_post'),

]