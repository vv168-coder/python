from utils.serializers import BaseSerializer

class BaseImageSerializer(BaseSerializer):
    # 序列化基础图片，其他列表需要关联图片时，引用该类
    def to_dict(self):
        image = self.obj
        return {
            'img' : image.img.url,
            'summary': image.summary,
        }