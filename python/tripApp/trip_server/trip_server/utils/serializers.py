class BaseSerializer(object):
    def __init__(self, obj):
        self.obj = obj

    def to_dict(self):
        return {}

class MeatSerializer(object):
    # 分页相关的元数据
    def __init__(self, page,page_count,total_count,**kwargs):
        """
        :param page: 当前页
        :param page_count:总页数
        :param total_count: 总记录数
        :param kwargs:
        """

        self.page = page
        self.page_count = page_count
        self.total_count = total_count

    def to_dict(self):
        return {
            "current_page" : self.page,
            "page_count" : self.page_count,
            "total_count" : self.total_count,
        }


class BaseListPageSerializer(object):
    # 分页封装类
    def __init__(self,page_obj,paginator=None,object_list=[]):
        """
        :param page_obj: 当前页的对象
        :param paginator: 分页器对象，
        :param object_list: 当前页的数据列表
        """
        self.page_obj = page_obj
        self.paginator = paginator
        self.object_list = object_list if object_list else page_obj.object_list

    def get_object(self,obj):
        # 转换成对象，子类重写
        return {}

    def to_dict(self):
        page = self.page_obj.number
        page_count = self.page_obj.paginator.num_pages
        total_count = self.page_obj.paginator.count
        meta = MeatSerializer(page=page,page_count=page_count,total_count=total_count).to_dict()

        objects = []
        for obj in self.object_list:
            objects.append(self.get_object(obj))


        return {
            'meta' : meta,
            'objects' : objects,
        }
