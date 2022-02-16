from django.shortcuts import render
from.models import Article


def articles_list(request):

    articles = Article.objects.all().order_by('date')
    
    return render(request, 'articles/articles_list.html',{'articles': articles})


def article_detail(request, slug):
    
   article = Article.objects.get(slug=slug)

   return render(request, 'articles/article_detail.html', {'article' : article})

   
# Create your views here.
