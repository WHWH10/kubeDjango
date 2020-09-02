from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class PushInfo(models.Model):
    device_id = models.CharField(max_length=256, verbose_name='기기값')
    firebase_token = models.CharField(max_length=256, verbose_name='토큰값')
    message_title = models.CharField(max_length=256, verbose_name='메시지 제목')
    message_content = models.TextField(verbose_name='메시지 내용')
    author = models.CharField(max_length=256, verbose_name='보낸사람')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='보낸날짜')

    def __str__(self):
        return self.device_id

    class Meta:
        db_table = 'push_info'
        verbose_name = '푸시메시지 정보'
        verbose_name_plural = '푸시메시지 정보'