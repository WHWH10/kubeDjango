from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class AdUser(models.Model):
    user_id = models.CharField(max_length=128, verbose_name='아이디')
    user_password = models.CharField(max_length=128, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'push_admin_user'
        verbose_name = '관리자페이지 사용자'
        verbose_name_plural = '관리자페이지 사용자'
