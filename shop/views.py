from rest_framework import viewsets
from shop.models import Review
from shop.serializers import ReviewSerializer


# list detail delete update까지 한 번에 구현됨.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
