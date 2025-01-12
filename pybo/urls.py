from django.urls import path
from . import views

# path에 url을 parameter로 받을 수 있게 처리하는 것도 여기서 함.
urlpatterns = [
    path("", views.index),
    path('<int:question_id>/', views.detail)
]
