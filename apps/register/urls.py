from django.urls import path, include

from apps.register import views

app_name = 'register'
urlpatterns = [
    path('', views.index, name='index'),  # /
    path('login/', views.login_, name='login'),  # /login/
    path('register/', views.register, name='register'),  # /register/
    path('logout/', views.log_out, name='logout'),  # /logout/
    path('profile/', views.profile, name='profile'),  # /profile/
    path('track/', views.track, name='track'),

    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

]
