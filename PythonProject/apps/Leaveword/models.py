from django.db import models
from apps.UserInfo.models import UserInfo


class Leaveword(models.Model):
    leaveWordId = models.AutoField(primary_key=True, verbose_name='留言id')
    leaveTitle = models.CharField(max_length=80, default='', verbose_name='留言标题')
    leaveContent = models.CharField(max_length=2000, default='', verbose_name='留言内容')
    userObj = models.ForeignKey(UserInfo,  db_column='userObj', on_delete=models.PROTECT, verbose_name='留言人')
    leaveTime = models.CharField(max_length=20, default='', verbose_name='留言时间')
    replyContent = models.CharField(max_length=1000, default='', verbose_name='管理回复')
    replyTime = models.CharField(max_length=20, default='', verbose_name='回复时间')

    class Meta:
        db_table = 't_Leaveword'
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        leaveword = {
            'leaveWordId': self.leaveWordId,
            'leaveTitle': self.leaveTitle,
            'leaveContent': self.leaveContent,
            'userObj': self.userObj.name,
            'userObjPri': self.userObj.user_name,
            'leaveTime': self.leaveTime,
            'replyContent': self.replyContent,
            'replyTime': self.replyTime,
        }
        return leaveword

