from django.urls import path
from . import views
from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    # base_views
    # 127.0.0.1:8000/pybo/
    path('', base_views.index, name='index'),
    # 127.0.0.1:8000/board/
    path('board/', base_views.board, name='board'),
    # 127.0.0.1:8000/pybo/
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_view
    # 127.0.0.1:8000/pybo/1/ 질문 등록
    path('question/create/', question_views.question_create, name="question_create"),
    # 질문 수정
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>', question_views.question_delete, name='question_delete'),

    # answer_view
    # 답변 등록
    path('answer/create/<int:question_id>/', answer_views.answer_create, name="answer_create"),
]