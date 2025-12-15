from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import sqlite3

# Create your views here.

def index(request):
  return HttpResponse("Cyber Security Project 1 by Lisa Lotz.")

# flaw
@csrf_exempt

# fix
# no '@csrf_exempt'
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

# flaw
@csrf_exempt

# fix
# no '@csrf_exempt'
def add(request):
  if request.method == "POST":
    author = request.POST.get('author', '')
    entry = request.POST.get('entry', '')

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    # flaw
    query = f"INSERT INTO src_diaries (author, entry) VALUES ('{author}', '{entry}')"
    cursor.executescript(query)
    conn.commit()

    # fix
    # query = "INSERT INTO src_diaries (author, entry) VALUES (?,?)"
    # cursor.execute(query, (author, entry))
    # conn.commit()

    return redirect('/injection/')

  return render(request, 'pages/injection.html')

# flaw
@csrf_exempt

# fix
# no '@csrf_exempt'
def access(request):
  # flaw
  users = User.objects.all()
  return render(request, 'pages/admin.html', {'users': users})

  # fix
  # @login_required
  # def access(request):
  #    users = User.objects.all()
  #    return render(request, 'pages/admin.html', {'users':users})

# flaw
@csrf_exempt

# fix
# no '@csrf_exempt'
def cryptography(request):
  if request.method == "POST":
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # flaw
    user = User.objects.create(username=username)
    user.password = password
    user.save()
    length = len(password)

    # fix
    # hashed_password = make_password(password)
    # user = User.objects.create(username=username)
    # user.password = password
    # user.save()
    # length = len(hashed_password)

    return HttpResponse(f"User created with password length of {length}.")

  return render(request, 'pages/cryptography.html') 