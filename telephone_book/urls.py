from django.urls import path, include
from rest_framework.routers import DefaultRouter

from telephone_book import views

app_name = "telephone_book"

router = DefaultRouter()
router.register("articles", views.ArticleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]