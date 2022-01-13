from rest_framework import serializers
from telephone_book.models import Number


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = "__all__"
