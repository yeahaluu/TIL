from django.db import models

# Naming Convention => 단일레코드의 이름(단수형)
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    hobby = models.TextField

