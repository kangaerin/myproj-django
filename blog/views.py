import json

from django.http import HttpResponse
from rest_framework import viewsets
from blog.serializers import PostSerializer
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def blog_list(request):
    qs = Post.objects.all()
    data = [
        {
            "id": Post.id,
            "title": Post.title,
            "content": Post.content,
        }
        for Post in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)
