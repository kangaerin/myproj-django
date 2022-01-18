from typing import Dict

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
)


class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):

    # access/refresh  속성외에 추가속성
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        # TODO : 프로필 이미지 url
        return data


# JWT Payload 커스텀
# @classmethod
# # 반환값은 사전 ▽
# def get_token(cls, user) -> Dict:
#     token = super().get_token(user)
#     token['username'] = user.username
#     token['first_name'] = user.first_name
#     token['last_name'] = user.last_name
#     return token


class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass
