from apps.Notice.views import FrontAddView, FrontListView, UpdateView, DeletesView, FrontShowView, AddView, \
    ListView, OutToExcelView, BackModifyView, FrontModifyView, ListAllView
from django.conf.urls import url

# 正在部署的应用的名称
app_name = 'Notice'

urlpatterns = [
    url(r'^frontAdd$', FrontAddView.as_view(), name='frontAdd'),  # 前台添加
    url(r'^frontModify/(?P<noticeId>.+)$', FrontModifyView.as_view(), name='frontModify'),  # 前台更新
    url(r'^frontList$', FrontListView.as_view(), name='frontList'),  # 前台查询列表
    url(r'^frontShow/(?P<noticeId>.+)$', FrontShowView.as_view(), name='frontShow'),  # 前台显示详情页
    url(r'^listAll', ListAllView.as_view(), name='listAll'),  # 前台查询所有信息

    url(r'^update/(?P<noticeId>.+)$', UpdateView.as_view(), name='update'),  # Ajax方式更新记录

    url(r'^add$', AddView.as_view(), name='add'),  # 后台添加
    url(r'^backModify/(?P<noticeId>.+)$', BackModifyView.as_view(), name="backModify"),  # 后台更新
    url(r'^list$', ListView.as_view(), name='list'),  # 后台信息列表
    url(r'^deletes$', DeletesView.as_view(), name="deletes"),  # 删除记录信息
    url(r'^OutToExcel$', OutToExcelView.as_view(), name='OutToExcel')  # 导出信息到excel并下载
]
