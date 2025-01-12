from django.urls import path
from . import views

app_name = 'pybo' # for url nickname redundunt problem

# path에 url을 parameter로 받을 수 있게 처리하는 것도 여기서 함.
urlpatterns = [
    path("", views.index, name="index"), # name : url 별칭(nickname?)
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
