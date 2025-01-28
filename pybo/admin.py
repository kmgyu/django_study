from django.contrib import admin
from .models import Question, Answer

# Register your models here.
# admin이 모델 관리 가능.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)