import re

from rest_framework import serializers
from news.models import Article


# 상황에 따라 다르게 선언이 가능함. 선언적 UI
# 비로그인 사용자용

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
    #
    # def validate_title(self, title):
    #     if len(title) < 3:
    #         raise serializers.ValidationError("3글자 이상!!!")
    #     if not re.search(r"[ㄱ-힣]", title):
    #         raise serializers.ValidationError("한글을 한 글자 이상 포함시켜주세요.")
    #     return title


class ArticleAnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content"]


# 골드멤버쉽 사용자용
class ArticleGoldMemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "photo"]


# 관리자용
class ArticleAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "photo", "created_at", "updated_at"]
