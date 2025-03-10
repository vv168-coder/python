#该文件用于暴露视图函数的链接地址

from django.urls import path

from sight.views import SightListView, SightDetailView, SightCommentListView, SightTicketListView, SightInfoDetailView, \
    AddCommentView

#配置访问地址列表
urlpatterns = [
    #path配置具体的函数地址，参数一：自定义访问地址。 参数2：函数名称 参数3：连接名字

    path('sight/list/', SightListView.as_view(), name='sight_list'),
    path('sight/detail/<int:pk>/', SightDetailView.as_view(), name='sight_detail'),
    path('comment/list/<int:pk>/',SightCommentListView.as_view(), name='sight_comment_list'),
    path('ticket/list/<int:pk>/',SightTicketListView.as_view(), name='sight_ticket_list'),
    path('sight/info/<int:pk>/',SightInfoDetailView.as_view(), name='sight_info_info'),
    path('sight/addcomment/<int:pk>/',AddCommentView.as_view(), name='add_comment'),
]