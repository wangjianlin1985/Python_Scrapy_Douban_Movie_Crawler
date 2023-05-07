from django.db import models
from tinymce.models import HTMLField


class Movie(models.Model):
    movieId = models.AutoField(primary_key=True, verbose_name='记录id')
    url = models.CharField(max_length=100, default='', verbose_name='豆瓣地址')
    title = models.CharField(max_length=80, default='', verbose_name='电影名称')
    director = models.CharField(max_length=50, default='', verbose_name='导演')
    screenwriter = models.CharField(max_length=50, default='', verbose_name='编剧')
    actors = models.CharField(max_length=800, default='', verbose_name='主演')
    category = models.CharField(max_length=50, default='', verbose_name='类型')
    country = models.CharField(max_length=20, default='', verbose_name='国家')
    langrage = models.CharField(max_length=50, default='', verbose_name='语言')
    initial = models.CharField(max_length=30, default='', verbose_name='上映日期')
    runtime = models.CharField(max_length=20, default='', verbose_name='片长')
    playUrl = models.CharField(max_length=100, default='', verbose_name='播放地址')
    rate = models.CharField(max_length=20, default='', verbose_name='豆瓣评分')
    starPeople = models.CharField(max_length=20, default='', verbose_name='评价人数')
    preShowUrl = models.CharField(max_length=100, default='', verbose_name='预告地址')
    intro = HTMLField(max_length=5000, verbose_name='剧情简介')
    icon = models.CharField(max_length=100, default='', verbose_name='海报图片')

    class Meta:
        db_table = 't_Movie'
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        movie = {
            'movieId': self.movieId,
            'url': self.url,
            'title': self.title,
            'director': self.director,
            'screenwriter': self.screenwriter,
            'actors': self.actors,
            'category': self.category,
            'country': self.country,
            'langrage': self.langrage,
            'initial': self.initial,
            'runtime': self.runtime,
            'playUrl': self.playUrl,
            'rate': self.rate,
            'starPeople': self.starPeople,
            'preShowUrl': self.preShowUrl,
            'intro': self.intro,
            'icon': self.icon,
        }
        return movie

