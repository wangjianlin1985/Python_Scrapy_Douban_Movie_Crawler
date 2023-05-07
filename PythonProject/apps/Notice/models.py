from django.db import models
from tinymce.models import HTMLField


class Notice(models.Model):
    noticeId = models.AutoField(primary_key=True, verbose_name='公告id')
    title = models.CharField(max_length=80, default='', verbose_name='标题')
    content = HTMLField(max_length=5000, verbose_name='公告内容')
    publishDate = models.CharField(max_length=20, default='', verbose_name='发布时间')

    class Meta:
        db_table = 't_Notice'
        verbose_name = '新闻公告信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        notice = {
            'noticeId': self.noticeId,
            'title': self.title,
            'content': self.content,
            'publishDate': self.publishDate,
        }
        return notice

