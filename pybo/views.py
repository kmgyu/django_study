from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .views import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
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
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    '''
    detail page of question and answer
    '''
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    '''
    pybo answer register
    '''
    question = get_object_or_404(Question, pk=question_id)
    # same as below
    # question.answer_set.create(content=request.POST.get('content'),
    #                            create_date=timezone.now(),
    #                            modify_date=timezone.now())
    # answer = Answer(question=question, content=request.POST.get('content'),
    #                 create_date=timezone.now(), modify_date=timezone.now())
    # answer.save()
    # return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST) # Auto mapping to Question object
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

