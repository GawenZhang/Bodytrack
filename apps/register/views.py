from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import tensorflow as tf
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np


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
def log_out(request):
    logout(request)  # 清除用户会话信息
    return redirect('/')  # 重定向到首页或登录页面


def profile(request):
    return render(request, 'profile.html')




# 加载保存的模型

from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K

# 自定义损失函数
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from tensorflow.keras.utils import get_custom_objects


# # 自定义损失函数
# def weighted_mse(y_true, y_pred):
#     # 定义不同特征的权重
#     age_weight = 0.1  # 减小年龄的权重
#     height_weight = 1.0  # 保持身高的权重
#     weight_weight = 1.0  # 保持体重的权重
#
#     # 计算每个特征的均方误差（MSE）
#     age_mse = K.mean(K.square(y_true[:, 0] - y_pred[:, 0]))  # 年龄误差
#     height_mse = K.mean(K.square(y_true[:, 1] - y_pred[:, 1]))  # 身高误差
#     weight_mse = K.mean(K.square(y_true[:, 2] - y_pred[:, 2]))  # 体重误差
#
#     # 加权平均误差
#     weighted_mse_value = (age_weight * age_mse + height_weight * height_mse + weight_weight * weight_mse) / (
#                 age_weight + height_weight + weight_weight)
#
#     return weighted_mse_value
#
#
# # 注册自定义损失函数
# get_custom_objects()['weighted_mse'] = weighted_mse
#
# # 加载模型
# model = load_model('E:/Workspace/BodyTrack/register/static/model/BMI_with_weighted_loss.h5')


# 之后可以继续使用该模型进行预测等操作


# 之后可以继续使用该模型进行预测等操作


def track(request):
    # msg = ""
    #
    # if request.method == 'POST':
    #     height = request.POST.get('height')
    #     weight = request.POST.get('weight')
    #     age = request.POST.get('age')
    #
    #     try:
    #         if height and weight and age:
    #             # 转换为适当的数值类型
    #             height = float(height)
    #             weight = float(weight)
    #             age = int(age)
    #
    #             # 执行预测
    #             bmi = model.predict([[height, weight, age]])
    #             msg = f"Predicted BMI: {bmi[0][0]}"  # 假设返回值是二维数组，取第一个元素
    #         else:
    #             raise ValueError("Height, Weight, or Age is empty!")
    #
    #     except ValueError as e:
    #         msg = f"Error: {e}"

    return render(request, 'track.html')
