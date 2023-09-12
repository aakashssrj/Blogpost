from django.shortcuts import render
from django.http import HttpResponse

# def home (request):
#     context ={}
#     return render (request,"AakashBlog/index.html",context)

def aboutus(request):
    return HttpResponse("<b>Hello World</b>")

def course(request):
    return HttpResponse("<ul><li>PHP</li><li>Python</li><li>HTML</li><li>SWEEETY</li></ul>")


# Building Django Dynamic Route --> Providind Detailed of post on same tab that is detailed post in a single post which is possible only by the help of dynamic route get managed.

def courseDetails(request,courseId):
    return HttpResponse(courseId)
#Rendering HTML pages for that:

# def home(request):
#     return render(request,"index.html")


def homepage(request):
    data1={
        'title': "AakashVaani",
    #     'clist':["PHP","SQL","PYTHON"],
    #     'dict2':[
    #         { 'name':"Aakash",'Branch':"CSE"},
    #          {   'name':"Bikash",'Branch':"Pilot"}

    #     ]
    }
    return render(request,"index.html",data1)

def login(request):
    return render(request,"index22.html")

def register(request):
    return render(request,"register.html")
