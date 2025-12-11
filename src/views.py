from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import User
import sqlite3

# Create your views here.

def index(request):
  return HttpResponse("Hello world.")

def injection(request):
  if request.method == "POST":
    author = request.POST.get('author', '')

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    # flaw
    query = f"SELECT entry FROM src_diaries WHERE author = '{author}'"
    cursor.execute(query)
    rows = cursor.fetchall()

    # fix
    # query = "SELECT entry FROM diaries WHERE username = %s"
    # cursor.execute(query, [author])
    # rows = cursor.fetchall()

    return render(request, 'pages/injection.html', {'entries': rows})

  return render(request, 'pages/injection.html')

def add(request):
  if request.method == "POST":
    author = request.POST.get('author', '')
    entry = request.POST.get('entry', '')

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    # flaw
    query = f"INSERT INTO src_diaries (author, entry) VALUES ('{author}', '{entry}')"
    cursor.execute(query)
    conn.commit()

    # fix
    # query = "INSERT INTO diaries VALUES (?,?)"
    # cursor.execute(query, (author, entry))
    # conn.commit()

    return redirect('/injection/')

  return render(request, 'pages/injection.html')

def access(request):
  # flaw
  return HttpResponse("Security is important!")

  # fix
  # @login_required
  # def access(request):
  #   return HttpResponse("Security is important!")    

def cryptography(request):
  if request.method == "POST":
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')

    # flaw
    User.objects.create(name=name, password=password)

    # fix
    # hashed_password = make_password(password)
    # User.objects.create(name=name, password=hashed_password)

    return HttpResponse("User created.")

  return render(request, 'pages/cryptography.html') 