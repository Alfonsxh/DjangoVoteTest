from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone


# Create your views here.


def index(request):
    """
    初始化界面
    :param request:
    :return:
    """
    all_question = Question.objects.order_by('pub_date')
    context = {
        'all_question': all_question
    }
    return render(request, 'polls/index.html', context = context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'  # 模板路径
    context_object_name = 'all_question'  # 模型传入的上下文中的名称
    # model = Question        # 模型名称
    # queryset = Question.objects.all()   # 数据set
    ordering = '-pub_date'  # 排序方式

    def get_queryset(self):
        """返回早于当前时间的问题"""
        return Question.objects.filter(pub_date__lte = timezone.now())


def detail(request, question_id):
    """
    问卷详情
    :param request:
    :param question_id: 问题ID
    :return: detail.html
    """
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question'


def results(request, question_id):
    """
    问卷结果展示
    :param request:
    :param question_id: 问题ID
    :return: requests.html
    """
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/requests.html', {'question': question})  # 转到对应的界面


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/requests.html'
    context_object_name = 'question'


def vote(request, question_id):
    """
    投票
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('polls:results', args = (question.id,)))  # 重定向到results界面


def regex(request, year):
    url_path = reverse("detail", args = (year,))
    return redirect(url_path)
    # return HttpResponse("You are looking for {year}'s archive.".format(year = year))
