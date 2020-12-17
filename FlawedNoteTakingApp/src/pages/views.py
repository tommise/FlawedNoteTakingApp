from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
from .models import Note
import sqlite3

'''
Flaw #5 - Cross Site Scripting (OWASP #7)
'''
@csrf_exempt
@login_required
def addPageView(request):
	note = request.POST.get("note")
	Note.objects.create(owner = request.user, note = note)

	return redirect('/')

'''
Flaw #4 - Broken Access Control (OWASP #5)
'''
@login_required
def deletePageView(request, note_id):
	conn = sqlite3.connect('src/db.sqlite3')
	cursor = conn.cursor()

	query = "DELETE FROM pages_note WHERE id = %s" % note_id
	
	'''
	Flaw #1 - Injection (OWASP #1)
	'''
	cursor.executescript(query)
	conn.commit()

	return redirect('/')

@login_required
def homePageView(request):
	notes = Note.objects.filter(owner = request.user)
	
	return render(request, 'pages/index.html', {'notes': notes})