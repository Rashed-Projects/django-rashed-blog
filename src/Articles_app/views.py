from django.shortcuts import render
from .models import Articles_model,Category,Comments
from django.core.paginator import Paginator
from django.db.models import Prefetch
from .forms import CommentForm

# Create your views here.

def getMainArticle():
    article=Articles_model.objects.get(id=1)
    return article



def home(request):
    articles=Articles_model.objects.all()
    
    paginator = Paginator(articles, 4) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'articles':page_obj,
        'mainArticle':getMainArticle(),
        'type':Articles_model.get_article_type(),
        'topArticle':getTopArticles(),
    }
    return render(request,'Articles_app/home.html',context)


def getTopArticles():
    top=Articles_model.objects.latest('creade_date')
    return top
def articleDetails(request,slug):
    article=Articles_model.objects.get(slug=slug)
    comment=Comments.objects.all()
    
    
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form=comment_form.save(commit=False)
            comment_form.article=article
            comment_form.save()
    else:
        CommentForm()


    context={
        'article':article,
        'comment':comment,
        'form':CommentForm,
    }
    return render(request,'Articles_app/article_details.html',context)