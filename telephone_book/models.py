from django.core.validators import RegexValidator
from django.db import models


class Number(models.Model):
    name = models.CharField(max_length=10, db_index=True,
                            validators=[
                                RegexValidator(r"[ㄱ-힣]", message="한글 이름을 입력해주세요."),
                            ])
    Phone_number = models.CharField(max_length=14, db_index=True,
                                    validators=[
                                        RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요."),
                                    ],
                                    help_text="입력예) 042-1234-1234")
    memo = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='telephone_book/photo/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "사람"
        verbose_name_plural = "전화번호부"
