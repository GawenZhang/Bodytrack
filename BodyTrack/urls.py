"""BodyTrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import apps.register
from apps import register
from apps.register import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    # path('community/', include('apps.community.urls')),  # community app 交给 community/urls.py
    # path('login/', include('apps.register.urls')),
    #
    # path('register/', include('apps.register.urls')),
    #
    # path('logout/', include('apps.register.urls')),
    #
    # path('community/', include('apps.register.urls')),
    #
    # path('profile/', include('apps.register.urls')),
    # path('plan/', include('apps.register.urls')),
    # path('track/', include('apps.register.urls')),
    path('', include('apps.register.urls')),         # 根路径和 register 相关路由
    path('community/', include('apps.community.urls')),
    path('plan/', include('apps.plan.urls')),
]
