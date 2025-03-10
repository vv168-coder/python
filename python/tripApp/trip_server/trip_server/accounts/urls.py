from django.urls import path

from accounts import views

urlpatterns = [
#     用户登录的
    path('user/login/',views.user_login,name='user_login'),
#     用户详细信息
    path('user/info/', views.user_info, name='user_info'),

    #     用户退出登录
    path('user/logout/', views.user_logout, name='user_logout'),

    # 用户登录，异步提交
    path('user/api/login/', views.user_api_login, name='user_api_login'),
#     用户登出
    path('user/api/logout/', views.user_api_logout, name='user_api_logout'),

#     用户详细信息
    path('user/api/info/', views.UserDetailView.as_view(), name='user_api_info'),

#   用户注册
    path('user/api/register/', views.UserRegisterView.as_view(), name='user_api_register'),

]