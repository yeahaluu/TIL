from django.db import models
from django.contrib.auth.models import AbstractUser
# contribution: 문서의 일부를 구성하는 독립적인 단위
# abstract: 추상적인
# AbstractUser: 존재하고 있는 기본 User 모델 필드들을 사용, username 필드만 없애고 싶을 때
# AbstractBaseUser: 완전히 새로운 사용자 모델을 생성하고 싶을 때
# settings.py - AUTH_USER_MODEL = 'accouts.User'/ admin.py - admin.site.register(User,UserAdmin)


class User(AbstractUser):
    pass