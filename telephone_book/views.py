from rest_framework.viewsets import ModelViewSet
from telephone_book.serializers import NumberSerializer
from telephone_book.models import Number


class ArticleViewSet(ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
