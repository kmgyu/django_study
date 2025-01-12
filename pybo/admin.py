from django.contrib import admin
from .models import Question, Answer

# Register your models here.
# admin이 모델 관리 가능.
admin.site.register(Question)
admin.site.register(Answer)