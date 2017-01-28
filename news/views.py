from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from models import News

class NewsView(View):
    def get(self, request):
        articles = News.objects.all()
        return render(request, 'news/news.html', {'articles': articles})

class ArticleView(View):
    def get(self, request, pk):
        article = get_object_or_404(News, pk=pk)
        return render(request, 'news/news_article.html', {'article': article})