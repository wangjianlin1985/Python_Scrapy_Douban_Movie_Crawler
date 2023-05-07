from django.db import models


class UserInfo(models.Model):
    user_name = models.CharField(max_length=30, default='', primary_key=True, verbose_name='用户名')
    password = models.CharField(max_length=30, default='', verbose_name='登录密码')
    name = models.CharField(max_length=20, default='', verbose_name='姓名')
    gender = models.CharField(max_length=4, default='', verbose_name='性别')
    birthDate = models.CharField(max_length=20, default='', verbose_name='出生日期')
    userPhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='用户照片')
    telephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    email = models.CharField(max_length=50, default='', verbose_name='邮箱')
    address = models.CharField(max_length=80, default='', verbose_name='家庭地址')
    regTime = models.CharField(max_length=20, default='', verbose_name='注册时间')

    class Meta:
        db_table = 't_UserInfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        userInfo = {
            'user_name': self.user_name,
            'password': self.password,
            'name': self.name,
            'gender': self.gender,
            'birthDate': self.birthDate,
            'userPhoto': self.userPhoto.url,
            'telephone': self.telephone,
            'email': self.email,
            'address': self.address,
            'regTime': self.regTime,
        }
        return userInfo

