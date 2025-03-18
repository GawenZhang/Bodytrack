from django.urls import path
from . import views  # 使用相对导入，更简洁

app_name = 'plan'  # 设置命名空间

urlpatterns = [
    path('', views.plan),  # /community/
    # path('post/', views.post, name='post'),  # /community/post/
    # 其他子路由根据需求添加
    path('report', views.report),  # /community/
]