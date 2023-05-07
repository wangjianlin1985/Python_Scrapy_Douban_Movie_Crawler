from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.Leaveword.models import Leaveword
from apps.UserInfo.models import UserInfo
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os
import datetime


class FrontAddView(BaseView):  # 前台留言添加
    def get(self,request):
        userInfos = UserInfo.objects.all()  # 获取所有用户
        context = {
            'userInfos': userInfos,
        }

        # 使用模板
        return render(request, 'Leaveword/leaveword_frontAdd.html', context)

    def post(self, request):
        leaveword = Leaveword() # 新建一个留言对象然后获取参数
        leaveword.leaveTitle = request.POST.get('leaveword.leaveTitle')
        leaveword.leaveContent = request.POST.get('leaveword.leaveContent')
        leaveword.userObj = UserInfo.objects.get(user_name= request.session.get('user_name'))
        leaveword.leaveTime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        leaveword.replyContent = '--'
        leaveword.replyTime = '--'
        leaveword.save() # 保存留言信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改留言
    def get(self, request, leaveWordId):
        context = {'leaveWordId': leaveWordId}
        return render(request, 'Leaveword/leaveword_frontModify.html', context)


class FrontListView(BaseView):  # 前台留言查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        userObj_user_name = self.getStrParam(request, 'userObj.user_name')
        leaveTime = self.getStrParam(request, 'leaveTime')
        leaveTitle = self.getStrParam(request, 'leaveTitle')
        # 然后条件组合查询过滤
        leavewords = Leaveword.objects.all()
        if userObj_user_name != '':
            leavewords = leavewords.filter(userObj=userObj_user_name)
        if leaveTime != '':
            leavewords = leavewords.filter(leaveTime__contains=leaveTime)
        if leaveTitle != '':
            leavewords = leavewords.filter(leaveTitle__contains=leaveTitle)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(leavewords, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        leavewords_page = self.paginator.page(self.currentPage)

        # 获取所有用户
        userInfos = UserInfo.objects.all()
        # 构造模板需要的参数
        context = {
            'userInfos': userInfos,
            'leavewords_page': leavewords_page,
            'userObj_user_name': userObj_user_name,
            'leaveTime': leaveTime,
            'leaveTitle': leaveTitle,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'Leaveword/leaveword_frontquery_result.html', context)

class FrontUserListView(BaseView):  # 前台留言查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        userObj_user_name =  request.session.get('user_name')
        leaveTime = self.getStrParam(request, 'leaveTime')
        leaveTitle = self.getStrParam(request, 'leaveTitle')
        # 然后条件组合查询过滤
        leavewords = Leaveword.objects.all()
        if userObj_user_name != '':
            leavewords = leavewords.filter(userObj=userObj_user_name)
        if leaveTime != '':
            leavewords = leavewords.filter(leaveTime__contains=leaveTime)
        if leaveTitle != '':
            leavewords = leavewords.filter(leaveTitle__contains=leaveTitle)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(leavewords, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        leavewords_page = self.paginator.page(self.currentPage)

        # 获取所有用户
        userInfos = UserInfo.objects.all()
        # 构造模板需要的参数
        context = {
            'userInfos': userInfos,
            'leavewords_page': leavewords_page,
            'userObj_user_name': userObj_user_name,
            'leaveTime': leaveTime,
            'leaveTitle': leaveTitle,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'Leaveword/leaveword_userFrontquery_result.html', context)



class FrontShowView(View):  # 前台显示留言详情页
    def get(self, request, leaveWordId):
        # 查询需要显示的留言对象
        leaveword = Leaveword.objects.get(leaveWordId=leaveWordId)
        context = {
            'leaveword': leaveword
        }
        # 渲染模板显示
        return render(request, 'Leaveword/leaveword_frontshow.html', context)


class ListAllView(View): # 前台查询所有留言
    def get(self,request):
        leavewords = Leaveword.objects.all()
        leavewordList = []
        for leaveword in leavewords:
            leavewordObj = {
                'leaveWordId': leaveword.leaveWordId,
                'leaveTitle': leaveword.leaveTitle,
            }
            leavewordList.append(leavewordObj)
        return JsonResponse(leavewordList, safe=False)


class UpdateView(BaseView):  # Ajax方式留言更新
    def get(self, request, leaveWordId):
        # GET方式请求查询留言对象并返回留言json格式
        leaveword = Leaveword.objects.get(leaveWordId=leaveWordId)
        return JsonResponse(leaveword.getJsonObj())

    def post(self, request, leaveWordId):
        # POST方式提交留言修改信息更新到数据库
        leaveword = Leaveword.objects.get(leaveWordId=leaveWordId)
        leaveword.leaveTitle = request.POST.get('leaveword.leaveTitle')
        leaveword.leaveContent = request.POST.get('leaveword.leaveContent')
        leaveword.userObj = UserInfo.objects.get(user_name=request.POST.get('leaveword.userObj.user_name'))
        leaveword.leaveTime = request.POST.get('leaveword.leaveTime')
        leaveword.replyContent = request.POST.get('leaveword.replyContent')
        leaveword.replyTime = request.POST.get('leaveword.replyTime')
        leaveword.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台留言添加
    def get(self,request):
        userInfos = UserInfo.objects.all()  # 获取所有用户
        context = {
            'userInfos': userInfos,
        }

        # 渲染显示模板界面
        return render(request, 'Leaveword/leaveword_add.html', context)

    def post(self, request):
        # POST方式处理图书添加业务
        leaveword = Leaveword() # 新建一个留言对象然后获取参数
        leaveword.leaveTitle = request.POST.get('leaveword.leaveTitle')
        leaveword.leaveContent = request.POST.get('leaveword.leaveContent')
        leaveword.userObj = UserInfo.objects.get(user_name=request.POST.get('leaveword.userObj.user_name'))
        leaveword.leaveTime = request.POST.get('leaveword.leaveTime')
        leaveword.replyContent = request.POST.get('leaveword.replyContent')
        leaveword.replyTime = request.POST.get('leaveword.replyTime')
        leaveword.save() # 保存留言信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新留言
    def get(self, request, leaveWordId):
        context = {'leaveWordId': leaveWordId}
        return render(request, 'Leaveword/leaveword_modify.html', context)


class ListView(BaseView):  # 后台留言列表
    def get(self, request):
        # 使用模板
        return render(request, 'Leaveword/leaveword_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        userObj_user_name = self.getStrParam(request, 'userObj.user_name')
        leaveTime = self.getStrParam(request, 'leaveTime')
        leaveTitle = self.getStrParam(request, 'leaveTitle')
        # 然后条件组合查询过滤
        leavewords = Leaveword.objects.all()
        if userObj_user_name != '':
            leavewords = leavewords.filter(userObj=userObj_user_name)
        if leaveTime != '':
            leavewords = leavewords.filter(leaveTime__contains=leaveTime)
        if leaveTitle != '':
            leavewords = leavewords.filter(leaveTitle__contains=leaveTitle)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(leavewords, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        leavewords_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        leavewordList = []
        for leaveword in leavewords_page:
            leaveword = leaveword.getJsonObj()
            leavewordList.append(leaveword)
        # 构造模板页面需要的参数
        leaveword_res = {
            'rows': leavewordList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(leaveword_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除留言信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        leaveWordIds = self.getStrParam(request, 'leaveWordIds')
        leaveWordIds = leaveWordIds.split(',')
        count = 0
        try:
            for leaveWordId in leaveWordIds:
                Leaveword.objects.get(leaveWordId=leaveWordId).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出留言信息到excel并下载
    def get(self, request):
        # 收集查询参数
        userObj_user_name = self.getStrParam(request, 'userObj.user_name')
        leaveTime = self.getStrParam(request, 'leaveTime')
        leaveTitle = self.getStrParam(request, 'leaveTitle')
        # 然后条件组合查询过滤
        leavewords = Leaveword.objects.all()
        if userObj_user_name != '':
            leavewords = leavewords.filter(userObj=userObj_user_name)
        if leaveTime != '':
            leavewords = leavewords.filter(leaveTime__contains=leaveTime)
        if leaveTitle != '':
            leavewords = leavewords.filter(leaveTitle__contains=leaveTitle)
        #将查询结果集转换成列表
        leavewordList = []
        for leaveword in leavewords:
            leaveword = leaveword.getJsonObj()
            leavewordList.append(leaveword)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(leavewordList)
        # 设置要导入到excel的列
        columns_map = {
            'leaveWordId': '留言id',
            'leaveTitle': '留言标题',
            'userObj': '留言人',
            'leaveTime': '留言时间',
            'replyContent': '管理回复',
            'replyTime': '回复时间',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'leavewords.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="leavewords.xlsx"'
        return response

