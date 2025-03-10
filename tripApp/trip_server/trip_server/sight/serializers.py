from bson import is_valid
# django把业务主体放在了业务层面
# 重构响应对象
# 为什么？
# 在服务端提供了很多的接口用于响应数据
# 为了便于前端能够统一处理这些数据，需要将所有响应的数据统一格式，成为重构响应对象（序列化）

from utils.serializers import BaseListPageSerializer, BaseSerializer


class SightListSerializer(BaseListPageSerializer):
    # 景点列表
    def get_object(self,obj):
        return{
            'id': obj.id,
            'name': obj.name,
            'main_img': obj.main_img.url,
            'min_price': obj.min_price,
            'score': obj.score,
            'province': obj.province,
            'city': obj.city,
            'comment_count': 0

        }

class SightDetailSerializers(BaseSerializer):
    # 景点详情
    def to_dict(self):
        obj = self.obj
        # 未来要在前端展示的数据
        return {
            'id':obj.id,
            'name': obj.name,
            'desc': obj.desc,
            'img': obj.banner_img.url,
            'content': obj.content,
            'score': obj.score,
            'min_price': obj.min_price,
            'province': obj.province,
            'city': obj.city,
            'area': obj.area,
            'town':obj.town,
            # 获得景点评论数量
            'comment_count': obj.comment_count,
            # 获得景点评论图片数量
            'image_count': obj.image_count,
        }


class CommentListSerializers(BaseListPageSerializer):
    def __init__(self, page_obj, paginator=None, object_list=[]):
        super().__init__(page_obj, paginator, object_list)
        self.errors = None

    def get_object(self,obj):
        user = obj.user
        # 图片用列表，用户不用，一个用户对应多个图片
        images = []
        for image in obj.images.filter(is_valid = True):
            images.append({
                'img': image.img.url,
                'summary': image.summary,
            })
        return {
                "user":{
                    'pk':user.pk,
                    'nickname':user.nickname,
                },
                'pk':obj.pk,
                'content':obj.content,
                'love_count':obj.love_count,
                'score':obj.score,
                'is_public':obj.is_public,
                'images':images,
                'created_at':obj.created_at.strftime('%Y-%m-%d'),
        }

class TicketListSerializers(BaseListPageSerializer):
#           门票列表
    def get_object(self,obj):
        return {
            'pk':obj.pk,
            'name': obj.name,
            'desc': obj.desc,
            'types': obj.types,
            'price': obj.price,
            'discount': obj.discount,
            'total_stock': obj.total_stock,
            'remain_stock': obj.remain_stock,
        }
class SightInfoSerializer(BaseSerializer):
    # 景点列表
    def to_dict(self):
        obj = self.obj
        return {
            'pk':obj.pk,
            'entry_explain':obj.entry_explain,
            'play_way':obj.play_way,
            'tips':obj.tips,
            'traffic':obj.traffic,
        }


from rest_framework import serializers
from .models import Comment

# 创建一个用于序列化评论数据的 Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_id','sight', 'content', 'score', 'is_public']

    # 这里可以做字段的校验，比如判断 score 的范围
    def validate_score(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("评分必须在 1 到 5 之间")
        return value
