from rest_framework import serializers
from shop.models import Review


# 장고의 기능만이 아닌 drf 기능을 활용함
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"