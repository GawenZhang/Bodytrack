
from django.urls import path, include

from apps.register import views

app_name = 'register'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/', views.login_),
    #
    # path('register/', views.register),
    #
    # path('logout/', views.log_out),
    #
    # path('profile/', views.profile),
    # path('plan/', views.plan),
    # path('track/', views.track),

    path('', views.index, name='index'),         # /
    path('login/', views.login_, name='login'),   # /login/
    path('register/', views.register, name='register'),  # /register/
    path('logout/', views.logout, name='logout'),  # /logout/
    path('profile/', views.profile, name='profile'),  # /profile/
    path('track/', views.track, name='track'),

]