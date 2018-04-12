# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .forms import SchoolForm, ServerForm
from .models import School, Server, Province, City, Teacher

# Register your models here.


class CityInline(admin.StackedInline):
    model = City
    extra = 3


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    inlines = [CityInline, ]


class SchoolInline(admin.StackedInline):
    model = School
    extra = 3


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [SchoolInline]


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 0

class ServerInline(admin.StackedInline):
    model = Server
    extra = 0
    fieldsets = (
        (u'操作系统', {
            'fields': ('os_type', 'access_type', 'access_addr', 'username', 'password'),
        }),
        (u'部署信息', {
            'classes': ('collapse',),
            'fields': ('manage_url', 'school_url', 'deploymentversion', 'special_modify', 'deploymentremake'),
        }),
        (u'网络及其他', {
            'classes': ('collapse',),
            'fields': ('public_network_addr', 'private_network_addr', 'domain_name', 'remark'),
        }),
        (u'硬件信息', {
            'classes': ('collapse',),
            'fields': ('core_number', 'memory_capacity', 'disk_capacity', 'device_type'),
        }),
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    inlines = [TeacherInline, ServerInline]
    list_filter = ['city']
    search_fields = ['name']
    form = SchoolForm


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_filter = ['school']
    search_fields = ['access_addr', 'school__name']
    fieldsets = (
        (u'操作系统', {
            'fields': ('os_type', 'access_type', 'access_addr', 'username', 'password'),
        }),
        (u'部署信息', {
            'classes': ('collapse',),
            'fields': ('manage_url', 'school_url', 'deploymentversion', 'special_modify', 'deploymentremake'),
        }),
        (u'网络及其他', {
            'classes': ('collapse',),
            'fields': ('public_network_addr', 'private_network_addr', 'domain_name', 'remark'),
        }),
        (u'硬件信息', {
            'classes': ('collapse',),
            'fields': ('core_number', 'memory_capacity', 'disk_capacity', 'device_type'),
        }),
    )
    # form = ServerForm


# admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.site_header = u'devops-storehouse'
