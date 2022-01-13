from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from news.serializers import ArticleSerializer
from telephone_book.models import Number


class ArticleViewSet(ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = ArticleSerializer