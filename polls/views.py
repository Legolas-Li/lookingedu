# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def about(request):
    exam_list = [{"id":1,"name":"2017第一次测试"}]
    return render_to_response("about.html",locals())


def get_exam_table(request):
    st = {"name":"阿杜", "num":"XTS123456", "phone":"13301332548", "data":[{"class":"语文","score":100},{"class":"数学","score":90},{"class":"法语","score":130}]}
    return render_to_response("table.html",locals())