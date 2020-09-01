from django.shortcuts import render
from .models import Articles_model,Category,Comments,Comments_comment
from django.core.paginator import Paginator

# Create your views here.

def getMainArticle():
    article=Articles_model.objects.get(id=1)
    return article



def home(request):
    articles=Articles_model.objects.all()
    
    paginator = Paginator(articles, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    context={
        'articles':page_obj,
        'mainArticle':getMainArticle(),
        'type':Articles_model.get_article_type()
    }
    return render(request,'Articles_app/home.html',context)

def articleDetails(request,slug):
    article=Articles_model.objects.get(slug=slug)
    comment=Comments.objects.all()
    comment_comments=Comments_comment.objects.get()
    
    context={
        'article':article,
        'comment':comment,
        'comment_comments':comment_comments,
    }
    return render(request,'Articles_app/article_details.html',context)