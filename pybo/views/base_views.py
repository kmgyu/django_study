from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

# Create your views here.

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("""
#     <h1>Hello, Django</h1>
#                         """)

# generic view를 이용 가능. 간단한데 @autowired같은 느낌인가?
def index(request):
    '''
    index pages
    '''
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by("-create_date")
    # question list를 페이지네이터에 집어넣어서 딕셔너리에 집어넣는다. 바로 집어넣는게 아니라!
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기. 여러 속성들이 있다.
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    '''
    detail page of question and answer
    '''
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
