# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Views for students
def students_list(request):
	return render(request, 'students/students_list.html', {})
	
def students_add(request):
	return HttpResponse('<h1>Students Add Form</h1>')
	
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Students %s</h1>' %sid)
	
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Students %s</h1>' %sid)

# Views for groups	
def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>')
	
def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(requst, gid):
	return('<h1>Edit Group %s</h1>' %gid)
	
def groups_delete(reqest, gid):
	return('<h1>Delete Group %s</h1>' %gid)