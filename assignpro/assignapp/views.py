from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from assignapp.models import Question, Answer, Like

@login_required
def post_question(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        question = Question.objects.create(user=request.user, title=title, content=content)
        return redirect('question_detail', question_id=question.id)
    return render(request, 'post_question.html')

def view_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'view_question.html', {'question': question, 'answers': answers})

@login_required
def post_answer(request, question_id):
    if request.method == 'POST':
        content = request.POST['content']
        question = Question.objects.get(id=question_id)
        answer = Answer.objects.create(user=request.user, question=question, content=content)
        return redirect('question_detail', question_id=question.id)
    return render(request, 'post_answer.html', {'question_id': question_id})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    Like.objects.create(user=request.user, answer=answer)
    return redirect('question_detail', question_id=answer.question.id)
