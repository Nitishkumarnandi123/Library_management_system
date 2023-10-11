from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from .models import Book, Course, Author, Semester

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request,'home.html',{'book':books})






def add(request):
    if request.method =='POST':
        l = Book()
        l.bname = request.POST['tbname']
        l.price = request.POST['tbprice']
        l.auther = Author.objects.get(autname=request.POST['ddlauther'])
        l.course = Course.objects.get(cname=request.POST['ddlcourse'])
        l.semester = Semester.objects.get(sname=request.POST['ddlsem'])
        l.save()
        return redirect(home)

    else:
        courses = Course.objects.all()
        authors = Author.objects.all()
        semesters = Semester.objects.all()
        data = {'courses': courses,'authors':authors,'semesters': semesters}
        return render(request,'addlibrary.html',data)

def search(request):
    value = request.GET['tbsearch']
    books = Book.objects.all()
    booklist =[]
    for book in books:
        if book.bname == value or str(book.price) == value or book.auther.autname == value or book.semester.sname ==value:
            booklist.append(book)
    return render(request,'searchResults.html',{'res':booklist})

def edit(request,id):
    l = Book.objects.get(id=id)
    if request.method == 'POST':
        l.bname = request.POST['tbname']
        l.price = request.POST['tbprice']
        l.auther = Author.objects.get(autname=request.POST['ddlauther'])
        l.course = Course.objects.get(cname=request.POST['ddlcourse'])
        l.semester = Semester.objects.get(sname=request.POST['ddlsem'])
        l.save()
        return redirect(home)
    else:
        authors = Author.objects.all()
        course = Course.objects.all()
        semesters = Semester.objects.all()
        data = {'bookdetail':l,'authors':authors,'course':course,'semesters':semesters}
        return render(request,'edit.html',data)



def deletefun(request,id):
    l = Book.objects.get(id=id)
    l.delete()
    return redirect(home)



def dummy1(request):
    return render(request,'homepage.html')


@never_cache
def loginfun(request):
        if request.method == "POST":
            user_name = request.POST['tbusername']
            user_password = request.POST['tbpass']
            myuser = authenticate(username=user_name, password=user_password)
            if myuser is not None:
                if myuser.is_superuser:
                    u1 = User.objects.get(username=user_name)
                    request.session['myuser'] = u1.id  # based on the id we are getting a details
                    request.session['myusername'] = u1.username
                    login(request, u1)
                    return render(request, 'homepage.html', {'data': u1.username})

            else:
                return render(request, 'login.html', {'msg': 'credential is not matching!!!'})
        return render(request, 'login.html')



@never_cache
def registerfun(request):
        if request.method == "POST":
            uname = request.POST['tbusername']
            useremail = request.POST['tbemail']
            userpswd = request.POST['tbpass']
            if User.objects.filter(username=uname).exists():
                return render(request, 'registration.html', {'user_available': True})
            elif User.objects.filter(email=useremail).exists():
                return render(request, 'registration.html', {'email_available': True})
            else:
                user = User.objects.create_user(email=useremail, password=userpswd, username=uname)
                user.save()
                return render(request, 'homepage.html')

        return render(request, 'registration.html')


@never_cache
def logoutfun(request):
    logout(request)
    request.session['myuser'] = None
    request.session['myusername'] = None
    return redirect(loginfun)