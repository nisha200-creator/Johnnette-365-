from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, "home.html")

def Articles(request):
    return render(request, 'articles.html')

def singlepage(request):
    return render(request,'singlepage.html')

def about(request):
    return render (request,'about.html')

def page(request):
    return render (request,'page.html')
def page2(request):
    return render (request,'page2.html')
