from django.contrib import admin
from telephone_book.models import Number


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    pass
