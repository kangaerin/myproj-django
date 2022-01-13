#blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet
from blog import views

app_name = "blog"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("posts.json", views.blog_list),
    path("api/", include(router.urls)),
]