from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    # jump to django에서는 makemigrations할 때 1번 옵션(null=True) 해줬는데... 난 나보다 약한 녀석의 말은 따르지 않는다
    # 2번은 계정 정보를 아무거나 집어넣는 거임.
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title

class Answer(models.Model):
    # question foreign key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
