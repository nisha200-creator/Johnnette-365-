from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, "home.html")

def article(request):
    return render(request, 'articles.html')
def singlepage(request):
    return render(request,'singlepage.html')