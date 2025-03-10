from django import http
from django.db.models import Q
from django.views.generic import ListView, DetailView

from sight import serializers
from sight.models import Ticket, Info
from utils.response import NotFoundJsonResponse



# Create your views here.

class SightListView(ListView):
    # 景点列表
    #每页放5页数据
    paginate_by = 5
    # 从数据库获取
    def get_queryset(self):
        # 重写查询方法
        query = Q(is_valid=True)
        #Q查询条件，该对象可以拼接多个条件
        #1、热门景点
        is_hot = self.request.GET.get('is_hot',None)
        if is_hot:
            query = query & Q(is_hot=True)
        #2、精选景点
        is_top = self.request.GET.get('is_top',None)
        if is_top:
            query = query & Q(is_top=True)
        #TODO 3、景点名称搜索
        # 获取前端传来的用于搜索的景点关键字
        name =  self.request.GET.get('name',None)
        if name:
            # 名字列模糊查询
            query = query & Q(name__icontains=name)
        queryset = Sight.objects.filter(query)
        return queryset

    # 用于分页函数
    def get_paginate_by(self, queryset):
    #     用于控制从前端传递过来的控制每一页显示条数的函数
        page_size = self.request.GET.get('limit',None)
        return page_size or self.paginate_by


    #用于响应数据
    #context 类的上下文对象，记录类的属性列表，其中包含的listview子类sightlistview的所有属性及数据
    def render_to_response(self, context, **response_kwargs):
        #利用上下文对象获取页面信息
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.SightListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        else:
            return NotFoundJsonResponse()
# 创建项目，实现


class SightDetailView(DetailView):
#（1） 数据库抓数据
# （2）响应数据
#     提供好的函数，获取数据
    def get_queryset(self):
        # 获取数据
        return Sight.objects.all()

    def render_to_response(self, context, **response_kwargs):
        # 响应数据
        # 获得结果集的所有信息
        page_obj = context['object']
        if page_obj is not None:

            if page_obj.is_valid == False:
                return NotFoundJsonResponse()

            data = serializers.SightDetailSerializers(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()


class SightCommentListView(ListView):
#     景点评论列表
    paginate_by = 10
    def get_queryset(self):
        #     根据id查询景点信息
        sight_id = self.kwargs.get('pk',None)
        sight = Sight.objects.filter(pk=sight_id,is_valid=True).first()
        if sight :
            return sight.comments.filter(is_valid=True)
        return Comment.objects.none()
    def render_to_response(self, context, **response_kwargs):
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.CommentListSerializers(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()

class SightTicketListView(ListView):
    # 景点门票列表
    paginate_by = 10
    def get_queryset(self):
    #     根据景点id查询
        sight_id = self.kwargs.get('pk',None)
        return Ticket.objects.filter(is_valid=True,sight=sight_id)

    def render_to_response(self, context, **response_kwargs):
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.TicketListSerializers(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()

class SightInfoDetailView(DetailView):
    # 当地址pk为none为空时，以下配置会生效
    pk_url_kwarg = None
    # url中参数的名称
    slug_url_kwarg = 'pk'
    # url中pk对应的哪一个字段（数据库中的字段）
    slug_field = 'sight__pk'
    # 景点详情
    def get_queryset(self):
    #     根据id获取景点详情
        return Info.objects.all()

    def render_to_response(self, context, **response_kwargs):

        page_obj = context['object']
        if page_obj is not None:
            data = serializers.SightInfoSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()




# import logging
#
# logger = logging.getLogger(__name__)
# class SightAddCommentView(viewsets.ViewSet):
#     @action(detail=True, methods=['post'])
#     def create_comment(self, request,pk=None):
#         # logger.debug(f"Request Data: {request.data}")
#         # user = request.user  # 获取当前登录的用户
#         sight_id = pk  # 从请求体中获取景点 ID
#         content = request.data.get('content')  # 评论内容
#         score = request.data.get('score')  # 评分
#
#         if not content or score is None:
#             return Response({'error': '缺少必要的参数'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 查找对应的景点
#         try:
#             sight = Sight.objects.get(pk=sight_id)
#         except Sight.DoesNotExist:
#             return Response({'error': '景点不存在'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 创建评论
#         comment = Comment.objects.create(
#             # user=user,
#             sight=sight,
#             user_id=1,
#             content=content,
#             score=score,
#             is_public=1,  # 默认为公开
#         )
#         comment.save()
#         # 返回成功响应
#         return Response({'success': True, 'message': '评论发布成功'}, status=status.HTTP_201_CREATED)

from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Comment, Sight

class AddCommentView(View):
    def post(self, request, pk):
        # 从请求中获取评论内容和评分
        content = request.POST.get('content')
        score = request.POST.get('score')

        # 检查是否缺少必要的参数
        if not content or score is None:
            return JsonResponse({'error': '缺少必要的参数'}, status=400)

        # 查找景点对象，如果没有找到则返回 404 错误
        sight = get_object_or_404(Sight, pk=pk)

        # 创建评论
        Comment.objects.create(
            sight=sight,
            content=content,
            score=score,
            is_public=True,
            user_id=1,  # 设置为 None，表示匿名评论
        )

        # 返回成功的响应
        return JsonResponse({'message': '评论成功'}, status=200)


