from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.UserInfo.models import UserInfo
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os
import datetime


class FrontAddView(BaseView):  # 前台用户添加
    def primaryKeyExist(self, user_name):  # 判断主键是否存在
        try:
            UserInfo.objects.get(user_name=user_name)
            return True
        except UserInfo.DoesNotExist:
            return False

    def get(self,request):

        # 使用模板
        return render(request, 'UserInfo/userInfo_frontAdd.html')

    def post(self, request):
        user_name = request.POST.get('userInfo.user_name') # 判断用户名是否存在
        if self.primaryKeyExist(user_name):
            return JsonResponse({'success': False, 'message': '用户名已经存在'})

        userInfo = UserInfo() # 新建一个用户对象然后获取参数
        userInfo.user_name = user_name
        userInfo.password = request.POST.get('userInfo.password')
        userInfo.name = request.POST.get('userInfo.name')
        userInfo.gender = request.POST.get('userInfo.gender')
        userInfo.birthDate = request.POST.get('userInfo.birthDate')
        try:
            userInfo.userPhoto = self.uploadImageFile(request,'userInfo.userPhoto')
        except ImageFormatException as ife:
            return JsonResponse({'success': False, 'message': ife.error})
        userInfo.telephone = request.POST.get('userInfo.telephone')
        userInfo.email = request.POST.get('userInfo.email')
        userInfo.address = request.POST.get('userInfo.address')
        userInfo.regTime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        userInfo.save() # 保存用户信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改用户
    def get(self, request, user_name):
        context = {'user_name': user_name}
        return render(request, 'UserInfo/userInfo_frontModify.html', context)

class FrontSelfModifyView(BaseView):  # 前台修改用户
    def get(self, request):
        context = {'user_name':  request.session.get('user_name')}
        return render(request, 'UserInfo/userInfo_frontModify.html', context)

class FrontListView(BaseView):  # 前台用户查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        user_name = self.getStrParam(request, 'user_name')
        name = self.getStrParam(request, 'name')
        birthDate = self.getStrParam(request, 'birthDate')
        telephone = self.getStrParam(request, 'telephone')
        # 然后条件组合查询过滤
        userInfos = UserInfo.objects.all()
        if user_name != '':
            userInfos = userInfos.filter(user_name__contains=user_name)
        if name != '':
            userInfos = userInfos.filter(name__contains=name)
        if birthDate != '':
            userInfos = userInfos.filter(birthDate__contains=birthDate)
        if telephone != '':
            userInfos = userInfos.filter(telephone__contains=telephone)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(userInfos, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        userInfos_page = self.paginator.page(self.currentPage)

        # 构造模板需要的参数
        context = {
            'userInfos_page': userInfos_page,
            'user_name': user_name,
            'name': name,
            'birthDate': birthDate,
            'telephone': telephone,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'UserInfo/userInfo_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示用户详情页
    def get(self, request, user_name):
        # 查询需要显示的用户对象
        userInfo = UserInfo.objects.get(user_name=user_name)
        context = {
            'userInfo': userInfo
        }
        # 渲染模板显示
        return render(request, 'UserInfo/userInfo_frontshow.html', context)


class ListAllView(View): # 前台查询所有用户
    def get(self,request):
        userInfos = UserInfo.objects.all()
        userInfoList = []
        for userInfo in userInfos:
            userInfoObj = {
                'user_name': userInfo.user_name,
                'name': userInfo.name,
            }
            userInfoList.append(userInfoObj)
        return JsonResponse(userInfoList, safe=False)


class UpdateView(BaseView):  # Ajax方式用户更新
    def get(self, request, user_name):
        # GET方式请求查询用户对象并返回用户json格式
        userInfo = UserInfo.objects.get(user_name=user_name)
        return JsonResponse(userInfo.getJsonObj())

    def post(self, request, user_name):
        # POST方式提交用户修改信息更新到数据库
        userInfo = UserInfo.objects.get(user_name=user_name)
        userInfo.password = request.POST.get('userInfo.password')
        userInfo.name = request.POST.get('userInfo.name')
        userInfo.gender = request.POST.get('userInfo.gender')
        userInfo.birthDate = request.POST.get('userInfo.birthDate')
        try:
            userPhotoName = self.uploadImageFile(request, 'userInfo.userPhoto')
        except ImageFormatException as ife:
            return JsonResponse({'success': False, 'message': ife.error})
        if userPhotoName != 'img/NoImage.jpg':
            userInfo.userPhoto = userPhotoName
        userInfo.telephone = request.POST.get('userInfo.telephone')
        userInfo.email = request.POST.get('userInfo.email')
        userInfo.address = request.POST.get('userInfo.address')
        userInfo.regTime = request.POST.get('userInfo.regTime')
        userInfo.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台用户添加
    def primaryKeyExist(self, user_name):  # 判断主键是否存在
        try:
            UserInfo.objects.get(user_name=user_name)
            return True
        except UserInfo.DoesNotExist:
            return False

    def get(self,request):

        # 渲染显示模板界面
        return render(request, 'UserInfo/userInfo_add.html')

    def post(self, request):
        # POST方式处理图书添加业务
        user_name = request.POST.get('userInfo.user_name') # 判断用户名是否存在
        if self.primaryKeyExist(user_name):
            return JsonResponse({'success': False, 'message': '用户名已经存在'})

        userInfo = UserInfo() # 新建一个用户对象然后获取参数
        userInfo.user_name = user_name
        userInfo.password = request.POST.get('userInfo.password')
        userInfo.name = request.POST.get('userInfo.name')
        userInfo.gender = request.POST.get('userInfo.gender')
        userInfo.birthDate = request.POST.get('userInfo.birthDate')
        try:
            userInfo.userPhoto = self.uploadImageFile(request,'userInfo.userPhoto')
        except ImageFormatException as ife:
            return JsonResponse({'success': False, 'message': ife.error})
        userInfo.telephone = request.POST.get('userInfo.telephone')
        userInfo.email = request.POST.get('userInfo.email')
        userInfo.address = request.POST.get('userInfo.address')
        userInfo.regTime = request.POST.get('userInfo.regTime')
        userInfo.save() # 保存用户信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新用户
    def get(self, request, user_name):
        context = {'user_name': user_name}
        return render(request, 'UserInfo/userInfo_modify.html', context)


class ListView(BaseView):  # 后台用户列表
    def get(self, request):
        # 使用模板
        return render(request, 'UserInfo/userInfo_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        user_name = self.getStrParam(request, 'user_name')
        name = self.getStrParam(request, 'name')
        birthDate = self.getStrParam(request, 'birthDate')
        telephone = self.getStrParam(request, 'telephone')
        # 然后条件组合查询过滤
        userInfos = UserInfo.objects.all()
        if user_name != '':
            userInfos = userInfos.filter(user_name__contains=user_name)
        if name != '':
            userInfos = userInfos.filter(name__contains=name)
        if birthDate != '':
            userInfos = userInfos.filter(birthDate__contains=birthDate)
        if telephone != '':
            userInfos = userInfos.filter(telephone__contains=telephone)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(userInfos, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        userInfos_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        userInfoList = []
        for userInfo in userInfos_page:
            userInfo = userInfo.getJsonObj()
            userInfoList.append(userInfo)
        # 构造模板页面需要的参数
        userInfo_res = {
            'rows': userInfoList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(userInfo_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除用户信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        user_names = self.getStrParam(request, 'user_names')
        user_names = user_names.split(',')
        count = 0
        try:
            for user_name in user_names:
                UserInfo.objects.get(user_name=user_name).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出用户信息到excel并下载
    def get(self, request):
        # 收集查询参数
        user_name = self.getStrParam(request, 'user_name')
        name = self.getStrParam(request, 'name')
        birthDate = self.getStrParam(request, 'birthDate')
        telephone = self.getStrParam(request, 'telephone')
        # 然后条件组合查询过滤
        userInfos = UserInfo.objects.all()
        if user_name != '':
            userInfos = userInfos.filter(user_name__contains=user_name)
        if name != '':
            userInfos = userInfos.filter(name__contains=name)
        if birthDate != '':
            userInfos = userInfos.filter(birthDate__contains=birthDate)
        if telephone != '':
            userInfos = userInfos.filter(telephone__contains=telephone)
        #将查询结果集转换成列表
        userInfoList = []
        for userInfo in userInfos:
            userInfo = userInfo.getJsonObj()
            userInfoList.append(userInfo)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(userInfoList)
        # 设置要导入到excel的列
        columns_map = {
            'user_name': '用户名',
            'name': '姓名',
            'gender': '性别',
            'birthDate': '出生日期',
            'telephone': '联系电话',
            'email': '邮箱',
            'regTime': '注册时间',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'userInfos.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="userInfos.xlsx"'
        return response

