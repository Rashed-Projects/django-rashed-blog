from django.shortcuts import render
from .models import Articles_model,Category
# Create your views here.


def home(request):
    articles=Articles_model.objects.all()
    
    context={
        'articles':articles
    }
    return render(request,'Articles_app/home.html',context)

def articleDetails(request,slug):
    article=Articles_model.objects.get(slug=slug)
    context={
        'article':article
    }
    return render(request,'Articles_app/article_details.html',context)