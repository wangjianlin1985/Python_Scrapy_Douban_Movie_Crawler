# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class MovieItem(Item):
    # 链接url
    url = Field()
    # 标题
    title = Field()
    # 导演
    director = Field()
    # 编辑
    screenwriter = Field()
    # 演员
    actors = Field()
    # 类别
    category = Field()
    # 发布国家
    country = Field()
    # 语言
    langrage = Field()
    # 上映日期
    initial = Field()
    # 片长
    runtime = Field()
    # 可观看url
    playUrl = Field()
    # 评分
    rate = Field()
    # 评分人数
    starPeople = Field()
    # 预告片url
    preShowUrl = Field()
    # 介绍
    intro = Field()
    # 缩略图
    icon = Field()

