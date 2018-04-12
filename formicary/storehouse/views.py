# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Server
import xlwt
import StringIO

@login_required()
def index(request):
    ws = xlwt.Workbook(encoding='utf-8')
    w = ws.add_sheet(u"学校数据信息")
    w.write(0, 0, u"学校名字")
    w.write(0, 1, u"版本号")
    w.write(0, 2, "school_url")
    w.write(0, 3, "manage_url")
    w.write(0, 4, u"备注")
    w.write(0, 5, u"特殊修改")
    w.write(0, 6, "cpu")
    w.write(0, 7, u"内存")
    w.write(0, 8, u"硬盘")

    for execl_row, server in enumerate(Server.objects.all(), start=1):
        print execl_row, server
        w.write(execl_row, 0, server.school.name)
        w.write(execl_row, 1, server.deploymentversion)
        w.write(execl_row, 2, server.school_url)
        w.write(execl_row, 3, server.manage_url)
        w.write(execl_row, 4, server.deploymentremake)
        w.write(execl_row, 5, server.special_modify)
        w.write(execl_row, 6, server.core_number)
        w.write(execl_row, 7, server.memory_capacity)
        w.write(execl_row, 8, server.disk_capacity)
    sio = StringIO.StringIO()
    ws.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=test.xls'
    response.write(sio.getvalue())
    return response



