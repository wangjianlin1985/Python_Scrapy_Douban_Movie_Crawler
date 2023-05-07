from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.Movie.models import Movie
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台电影添加
    def get(self,request):

        # 使用模板
        return render(request, 'Movie/movie_frontAdd.html')

    def post(self, request):
        movie = Movie() # 新建一个电影对象然后获取参数
        movie.url = request.POST.get('movie.url')
        movie.title = request.POST.get('movie.title')
        movie.director = request.POST.get('movie.director')
        movie.screenwriter = request.POST.get('movie.screenwriter')
        movie.actors = request.POST.get('movie.actors')
        movie.category = request.POST.get('movie.category')
        movie.country = request.POST.get('movie.country')
        movie.langrage = request.POST.get('movie.langrage')
        movie.initial = request.POST.get('movie.initial')
        movie.runtime = request.POST.get('movie.runtime')
        movie.playUrl = request.POST.get('movie.playUrl')
        movie.rate = request.POST.get('movie.rate')
        movie.starPeople = request.POST.get('movie.starPeople')
        movie.preShowUrl = request.POST.get('movie.preShowUrl')
        movie.intro = request.POST.get('movie.intro')
        movie.icon = request.POST.get('movie.icon')
        movie.save() # 保存电影信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改电影
    def get(self, request, movieId):
        context = {'movieId': movieId}
        return render(request, 'Movie/movie_frontModify.html', context)


class FrontListView(BaseView):  # 前台电影查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        title = self.getStrParam(request, 'title')
        director = self.getStrParam(request, 'director')
        screenwriter = self.getStrParam(request, 'screenwriter')
        actors = self.getStrParam(request, 'actors')
        category = self.getStrParam(request, 'category')
        country = self.getStrParam(request, 'country')
        langrage = self.getStrParam(request, 'langrage')
        initial = self.getStrParam(request, 'initial')
        # 然后条件组合查询过滤
        movies = Movie.objects.all()
        if title != '':
            movies = movies.filter(title__contains=title)
        if director != '':
            movies = movies.filter(director__contains=director)
        if screenwriter != '':
            movies = movies.filter(screenwriter__contains=screenwriter)
        if actors != '':
            movies = movies.filter(actors__contains=actors)
        if category != '':
            movies = movies.filter(category__contains=category)
        if country != '':
            movies = movies.filter(country__contains=country)
        if langrage != '':
            movies = movies.filter(langrage__contains=langrage)
        if initial != '':
            movies = movies.filter(initial__contains=initial)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(movies, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        movies_page = self.paginator.page(self.currentPage)

        # 构造模板需要的参数
        context = {
            'movies_page': movies_page,
            'title': title,
            'director': director,
            'screenwriter': screenwriter,
            'actors': actors,
            'category': category,
            'country': country,
            'langrage': langrage,
            'initial': initial,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'Movie/movie_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示电影详情页
    def get(self, request, movieId):
        # 查询需要显示的电影对象
        movie = Movie.objects.get(movieId=movieId)
        context = {
            'movie': movie
        }
        # 渲染模板显示
        return render(request, 'Movie/movie_frontshow.html', context)


class ListAllView(View): # 前台查询所有电影
    def get(self,request):
        movies = Movie.objects.all()
        movieList = []
        for movie in movies:
            movieObj = {
                'movieId': movie.movieId,
            }
            movieList.append(movieObj)
        return JsonResponse(movieList, safe=False)


class UpdateView(BaseView):  # Ajax方式电影更新
    def get(self, request, movieId):
        # GET方式请求查询电影对象并返回电影json格式
        movie = Movie.objects.get(movieId=movieId)
        return JsonResponse(movie.getJsonObj())

    def post(self, request, movieId):
        # POST方式提交电影修改信息更新到数据库
        movie = Movie.objects.get(movieId=movieId)
        movie.url = request.POST.get('movie.url')
        movie.title = request.POST.get('movie.title')
        movie.director = request.POST.get('movie.director')
        movie.screenwriter = request.POST.get('movie.screenwriter')
        movie.actors = request.POST.get('movie.actors')
        movie.category = request.POST.get('movie.category')
        movie.country = request.POST.get('movie.country')
        movie.langrage = request.POST.get('movie.langrage')
        movie.initial = request.POST.get('movie.initial')
        movie.runtime = request.POST.get('movie.runtime')
        movie.playUrl = request.POST.get('movie.playUrl')
        movie.rate = request.POST.get('movie.rate')
        movie.starPeople = request.POST.get('movie.starPeople')
        movie.preShowUrl = request.POST.get('movie.preShowUrl')
        movie.intro = request.POST.get('movie.intro')
        movie.icon = request.POST.get('movie.icon')
        movie.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台电影添加
    def get(self,request):

        # 渲染显示模板界面
        return render(request, 'Movie/movie_add.html')

    def post(self, request):
        # POST方式处理图书添加业务
        movie = Movie() # 新建一个电影对象然后获取参数
        movie.url = request.POST.get('movie.url')
        movie.title = request.POST.get('movie.title')
        movie.director = request.POST.get('movie.director')
        movie.screenwriter = request.POST.get('movie.screenwriter')
        movie.actors = request.POST.get('movie.actors')
        movie.category = request.POST.get('movie.category')
        movie.country = request.POST.get('movie.country')
        movie.langrage = request.POST.get('movie.langrage')
        movie.initial = request.POST.get('movie.initial')
        movie.runtime = request.POST.get('movie.runtime')
        movie.playUrl = request.POST.get('movie.playUrl')
        movie.rate = request.POST.get('movie.rate')
        movie.starPeople = request.POST.get('movie.starPeople')
        movie.preShowUrl = request.POST.get('movie.preShowUrl')
        movie.intro = request.POST.get('movie.intro')
        movie.icon = request.POST.get('movie.icon')
        movie.save() # 保存电影信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新电影
    def get(self, request, movieId):
        context = {'movieId': movieId}
        return render(request, 'Movie/movie_modify.html', context)


class ListView(BaseView):  # 后台电影列表
    def get(self, request):
        # 使用模板
        return render(request, 'Movie/movie_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        title = self.getStrParam(request, 'title')
        director = self.getStrParam(request, 'director')
        screenwriter = self.getStrParam(request, 'screenwriter')
        actors = self.getStrParam(request, 'actors')
        category = self.getStrParam(request, 'category')
        country = self.getStrParam(request, 'country')
        langrage = self.getStrParam(request, 'langrage')
        initial = self.getStrParam(request, 'initial')
        # 然后条件组合查询过滤
        movies = Movie.objects.all()
        if title != '':
            movies = movies.filter(title__contains=title)
        if director != '':
            movies = movies.filter(director__contains=director)
        if screenwriter != '':
            movies = movies.filter(screenwriter__contains=screenwriter)
        if actors != '':
            movies = movies.filter(actors__contains=actors)
        if category != '':
            movies = movies.filter(category__contains=category)
        if country != '':
            movies = movies.filter(country__contains=country)
        if langrage != '':
            movies = movies.filter(langrage__contains=langrage)
        if initial != '':
            movies = movies.filter(initial__contains=initial)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(movies, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        movies_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        movieList = []
        for movie in movies_page:
            movie = movie.getJsonObj()
            movieList.append(movie)
        # 构造模板页面需要的参数
        movie_res = {
            'rows': movieList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(movie_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除电影信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        movieIds = self.getStrParam(request, 'movieIds')
        movieIds = movieIds.split(',')
        count = 0
        try:
            for movieId in movieIds:
                Movie.objects.get(movieId=movieId).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出电影信息到excel并下载
    def get(self, request):
        # 收集查询参数
        title = self.getStrParam(request, 'title')
        director = self.getStrParam(request, 'director')
        screenwriter = self.getStrParam(request, 'screenwriter')
        actors = self.getStrParam(request, 'actors')
        category = self.getStrParam(request, 'category')
        country = self.getStrParam(request, 'country')
        langrage = self.getStrParam(request, 'langrage')
        initial = self.getStrParam(request, 'initial')
        # 然后条件组合查询过滤
        movies = Movie.objects.all()
        if title != '':
            movies = movies.filter(title__contains=title)
        if director != '':
            movies = movies.filter(director__contains=director)
        if screenwriter != '':
            movies = movies.filter(screenwriter__contains=screenwriter)
        if actors != '':
            movies = movies.filter(actors__contains=actors)
        if category != '':
            movies = movies.filter(category__contains=category)
        if country != '':
            movies = movies.filter(country__contains=country)
        if langrage != '':
            movies = movies.filter(langrage__contains=langrage)
        if initial != '':
            movies = movies.filter(initial__contains=initial)
        #将查询结果集转换成列表
        movieList = []
        for movie in movies:
            movie = movie.getJsonObj()
            movieList.append(movie)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(movieList)
        # 设置要导入到excel的列
        columns_map = {
            'title': '电影名称',
            'director': '导演',
            'screenwriter': '编剧',
            'actors': '主演',
            'category': '类型',
            'country': '国家',
            'langrage': '语言',
            'initial': '上映日期',
            'rate': '豆瓣评分',
            'icon': '海报图片',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'movies.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="movies.xlsx"'
        return response

