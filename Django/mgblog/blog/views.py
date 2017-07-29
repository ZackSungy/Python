# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import models

def index(request):
	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})

def article(request,article_id):
	article=models.Article.objects.get(pk=article_id);
	return render(request,'blog/article.html',{'article':article})

def edit_html(request,article_id):
	if article_id == '0':
		return render(request,'blog/edit.html');
	article=models.Article.objects.get(pk=article_id);
	return render(request,'blog/edit.html',{'article':article});

def edit_action(request):
	title=request.POST.get('title','TITLE');
	content=request.POST.get('content','CONTENT');
	a_id=request.POST.get('id','0');
	print a_id;
	if a_id == '0':
		models.Article.objects.create(title=title,content=content);
		articles=models.Article.objects.all();
		return render(request,'blog/index.html',{'articles':articles});
	article=models.Article.objects.get(pk=a_id);
	article.title=title;
	article.constent=content;
	article.save();
	return render(request,'blog/article.html',{'article':article})
	
	

