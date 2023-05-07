from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.Notice.models import Notice
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台新闻公告添加
    def get(self,request):

        # 使用模板
        return render(request, 'Notice/notice_frontAdd.html')

    def post(self, request):
        notice = Notice() # 新建一个新闻公告对象然后获取参数
        notice.title = request.POST.get('notice.title')
        notice.content = request.POST.get('notice.content')
        notice.publishDate = request.POST.get('notice.publishDate')
        notice.save() # 保存新闻公告信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改新闻公告
    def get(self, request, noticeId):
        context = {'noticeId': noticeId}
        return render(request, 'Notice/notice_frontModify.html', context)


class FrontListView(BaseView):  # 前台新闻公告查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        title = self.getStrParam(request, 'title')
        publishDate = self.getStrParam(request, 'publishDate')
        # 然后条件组合查询过滤
        notices = Notice.objects.all()
        if title != '':
            notices = notices.filter(title__contains=title)
        if publishDate != '':
            notices = notices.filter(publishDate__contains=publishDate)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(notices, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        notices_page = self.paginator.page(self.currentPage)

        # 构造模板需要的参数
        context = {
            'notices_page': notices_page,
            'title': title,
            'publishDate': publishDate,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'Notice/notice_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示新闻公告详情页
    def get(self, request, noticeId):
        # 查询需要显示的新闻公告对象
        notice = Notice.objects.get(noticeId=noticeId)
        context = {
            'notice': notice
        }
        # 渲染模板显示
        return render(request, 'Notice/notice_frontshow.html', context)


class ListAllView(View): # 前台查询所有新闻公告
    def get(self,request):
        notices = Notice.objects.all()
        noticeList = []
        for notice in notices:
            noticeObj = {
                'noticeId': notice.noticeId,
                'title': notice.title,
            }
            noticeList.append(noticeObj)
        return JsonResponse(noticeList, safe=False)


class UpdateView(BaseView):  # Ajax方式新闻公告更新
    def get(self, request, noticeId):
        # GET方式请求查询新闻公告对象并返回新闻公告json格式
        notice = Notice.objects.get(noticeId=noticeId)
        return JsonResponse(notice.getJsonObj())

    def post(self, request, noticeId):
        # POST方式提交新闻公告修改信息更新到数据库
        notice = Notice.objects.get(noticeId=noticeId)
        notice.title = request.POST.get('notice.title')
        notice.content = request.POST.get('notice.content')
        notice.publishDate = request.POST.get('notice.publishDate')
        notice.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台新闻公告添加
    def get(self,request):

        # 渲染显示模板界面
        return render(request, 'Notice/notice_add.html')

    def post(self, request):
        # POST方式处理图书添加业务
        notice = Notice() # 新建一个新闻公告对象然后获取参数
        notice.title = request.POST.get('notice.title')
        notice.content = request.POST.get('notice.content')
        notice.publishDate = request.POST.get('notice.publishDate')
        notice.save() # 保存新闻公告信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新新闻公告
    def get(self, request, noticeId):
        context = {'noticeId': noticeId}
        return render(request, 'Notice/notice_modify.html', context)


class ListView(BaseView):  # 后台新闻公告列表
    def get(self, request):
        # 使用模板
        return render(request, 'Notice/notice_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        title = self.getStrParam(request, 'title')
        publishDate = self.getStrParam(request, 'publishDate')
        # 然后条件组合查询过滤
        notices = Notice.objects.all()
        if title != '':
            notices = notices.filter(title__contains=title)
        if publishDate != '':
            notices = notices.filter(publishDate__contains=publishDate)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(notices, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        notices_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        noticeList = []
        for notice in notices_page:
            notice = notice.getJsonObj()
            noticeList.append(notice)
        # 构造模板页面需要的参数
        notice_res = {
            'rows': noticeList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(notice_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除新闻公告信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        noticeIds = self.getStrParam(request, 'noticeIds')
        noticeIds = noticeIds.split(',')
        count = 0
        try:
            for noticeId in noticeIds:
                Notice.objects.get(noticeId=noticeId).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出新闻公告信息到excel并下载
    def get(self, request):
        # 收集查询参数
        title = self.getStrParam(request, 'title')
        publishDate = self.getStrParam(request, 'publishDate')
        # 然后条件组合查询过滤
        notices = Notice.objects.all()
        if title != '':
            notices = notices.filter(title__contains=title)
        if publishDate != '':
            notices = notices.filter(publishDate__contains=publishDate)
        #将查询结果集转换成列表
        noticeList = []
        for notice in notices:
            notice = notice.getJsonObj()
            noticeList.append(notice)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(noticeList)
        # 设置要导入到excel的列
        columns_map = {
            'noticeId': '公告id',
            'title': '标题',
            'publishDate': '发布时间',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'notices.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="notices.xlsx"'
        return response

