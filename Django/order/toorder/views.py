# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import models;

def Home(request):
    businesses=models.Business.objects.all();
    return render(request,'order/Home.html',{'businesses':businesses});


def Order(request,Business_num):
    business = models.Business.objects.get(num=Business_num);
    print business.name;
    orders=models.Order.objects.filter(Business=business.name);
    return render(request,'order/order.html',{'orders':orders});

def chioce(request):
    return render(request,'order/Bill.html');

def Bill(request):
    paper=request.POST.get('paper','NOBODY');
    sq=request.POST.get('sq','NOTHING');
    money=request.POST.get('money','0');
    if money!=0:
        models.Bill.objects.create(paper=paper,sq=sq,money=money);
        Bills=models.Bill.objects.all();
        return render(request,'order/Bills.html',{'Bills':Bills})

def Bills(request):
    Bills = models.Bill.objects.all();
    return render(request, 'order/Bills.html', {'Bills': Bills})