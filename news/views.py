import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def article_list(request):
    qs = Article.objects.all()

    # 2
    serializer = ArticleSerializer(qs, many=True)
    data = serializer.data

    # 1
    # data = [
    #     {
    #         "id": article.id,
    #         "title": article.title,
    #         "content": article.content,
    #         "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,
    #     }
    #     for article in qs
    # ]
    json_string = json.dumps(data)
    return HttpResponse(json_string, content_type="application/json")
