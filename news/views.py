from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer


# viewset은 5개 지원
# list, detail, create, update, daelete를 한 개 viewset에서 지원
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in("POST, "PUT", "PATCH", DELETE"):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고나서 실제 serializer.save()를 할때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지정을 지원합니다.
        serializer.save(author=self.request.user)
