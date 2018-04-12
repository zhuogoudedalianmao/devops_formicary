# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.


@python_2_unicode_compatible
class Province(models.Model):
    """省份"""
    name = models.CharField(max_length=32, unique=True, help_text=u'名称')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    """城市"""
    name = models.CharField(max_length=32, unique=True, help_text=u'名称')
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return '.'.join([self.province.name, self.name])


@python_2_unicode_compatible
class School(models.Model):
    """学校"""
    name = models.CharField(max_length=64, unique=True, help_text=u'名称')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        desc = '%(province_name)s.%(city_name)s-%(school_name)s' % {
            'province_name': self.city.province.name,
            'city_name': self.city.name,
            'school_name': self.name
        }

        first_server = self.server_set.first()
        if first_server:
            ssh = '%(username)s@%(access_addr)s %(password)s' % {
                'username': first_server.username,
                'access_addr': first_server.access_addr,
                'password': first_server.password
            }
        else:
            ssh = '没有登记服务器'

        return '----'.join([desc, ssh])


@python_2_unicode_compatible
class Teacher(models.Model):
    """老师"""
    name = models.CharField(max_length=32, help_text=u'名称')
    title = models.CharField(max_length=64, blank=True, help_text=u'头衔')
    tel = models.CharField(max_length=32, blank=True, help_text=u'电话')
    qq = models.CharField(max_length=32, blank=True, help_text=u'QQ')
    remark = models.CharField(max_length=1024, blank=True, help_text=u'备注')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return '%(name)s <%(school_name)s - %(title)s>' % {
            'school_name': self.school.name,
            'title': self.title,
            'name': self.name
        }


@python_2_unicode_compatible
class Server(models.Model):
    """服务器"""
    DEVICE_TYPE = (
        ('RM', U'实体机'),
        ('VM', U'VM-WARE'),
    )
    core_number = models.IntegerField(help_text=u'CPU核心数量')
    memory_capacity = models.IntegerField(help_text=u'内存容量，单位GB')
    disk_capacity = models.IntegerField(help_text=u'硬盘容量，单位GB')
    device_type = models.CharField(max_length=2, choices=DEVICE_TYPE, help_text=u'设备类型')
    os_type = models.CharField(max_length=32, blank=True, help_text=u'操作系统')
    access_type = models.CharField(max_length=10, blank=True, default='SSH', help_text=u'远程访问方式')
    access_addr = models.CharField(max_length=128, blank=True, help_text=u'访问地址')
    username = models.CharField(max_length=128, blank=True, help_text=u'账号')
    password = models.CharField(max_length=128, blank=True, help_text=u'密码')
    public_network_addr = models.CharField(max_length=64, blank=True, help_text=u'公网地址')
    private_network_addr = models.CharField(max_length=64, help_text=u'内网地址')
    domain_name = models.CharField(max_length=64, blank=True, help_text=u'域名')
    remark = models.TextField(max_length=1024, blank=True, help_text=u'备注')
    school = models.ForeignKey(School, on_delete=models.CASCADE, help_text=u'学校')
    manage_url = models.URLField(max_length=128,blank=True,help_text=u'后台管理地址')
    school_url = models.URLField(max_length=128,blank=True,help_text=u'学生登录地址')
    deploymentversion = models.CharField(max_length=16,blank=True,help_text=u'版本号')
    special_modify = models.CharField(max_length=128,blank=True,help_text=u'特殊修改')
    deploymentremake = models.TextField(max_length=1024,blank=True,help_text=u'备注')

    def __str__(self):
        return ' access_type:%(access_type)s,access_addr: %(access_addr)s, username: %(username)s,password: %(password)s, school: %(school)s' % {
            'access_type': self.access_type,
            'access_addr': self.access_addr,
            'username': self.username,
            'password': self.password,
            'school': self.school
        }


