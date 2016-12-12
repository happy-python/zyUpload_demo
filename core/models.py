#coding:utf-8
from django.db import models
import datetime, time
import uuid
import os


def generate_filename(instance, filename):
    """
    安全考虑，生成随机文件名
    """
    directory_name = datetime.datetime.now().strftime('photos/%Y/%m/%d')
    filename = uuid.uuid4().hex + os.path.splitext(filename)[-1]
    return os.path.join(directory_name, filename)


def default_time():
    return int(time.time())


class Photo(models.Model):
    image = models.ImageField(verbose_name='图片', upload_to=generate_filename)
    create_time = models.IntegerField('添加时间', default=default_time, editable=False)
