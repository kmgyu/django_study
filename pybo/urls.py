from django.urls import path
from . import views

from .views import base_views, question_views, answer_views

app_name = 'pybo' # for url nickname redundunt problem

# path에 url을 parameter로 받을 수 있게 처리하는 것도 여기서 함.
urlpatterns = [
     # base_views.py
     path('',
     base_views.index, name='index'),
     path('<int:question_id>/',
     base_views.detail, name='detail'),

     # question_views.py
     path('question/create/',
     question_views.question_create, name='question_create'),
     path('question/modify/<int:question_id>/',
     question_views.question_modify, name='question_modify'),
     path('question/delete/<int:question_id>/',
     question_views.question_delete, name='question_delete'),
     path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

     # answer_views.py
     path('answer/create/<int:question_id>/',
     answer_views.answer_create, name='answer_create'),
     path('answer/modify/<int:answer_id>/',
     answer_views.answer_modify, name='answer_modify'),
     path('answer/delete/<int:answer_id>/',
     answer_views.answer_delete, name='answer_delete'),
     path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
