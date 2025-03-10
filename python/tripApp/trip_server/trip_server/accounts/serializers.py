# 用户的基本信息
from utils.serializers import BaseSerializer


# 重写父类：父类有这个函数，但子类想扩展这个函数，就可以在子类最后那个重写这个函数
class UserSerializer(BaseSerializer):
    def to_dict(self):
        user =  self.obj
        return {
            'nickname':user.nickname,
            'avatar':user.avatar_url
        }


class UserProfileSerializer(BaseSerializer):
    def to_dict(self):
        profile =  self.obj
        return {
            'real_name':profile.real_name,
            'sex':profile.sex,
            'sex_display':profile.get_sex_display()
        }