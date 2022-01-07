from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import review_list, ReviewViewSet


app_name = "shop"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("reviews/", review_list, name="review_list"),
    path("api/", include(router.urls)),
]