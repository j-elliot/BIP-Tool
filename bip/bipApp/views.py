from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question, Choice, Project, Task, Report, Time_Clock_Entry, Item
from django.urls import reverse
from django.views import generic
import datetime
from django.utils import timezone
from dal import autocomplete


def index(request):
   return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
  today = datetime.datetime.now().date()
  daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

class IndexView(generic.ListView):
    template_name = 'bipApp/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Project.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class ProjectView(generic.ListView):
    model = Task
    template_name = 'bipApp/project.html'
    context_object_name = 'task_list'

class TaskView(generic.ListView):
    model = Report
    template_name = 'bipApp/task.html'
    context_object_name = 'report_list'

class ReportView(generic.ListView):
    model = Time_Clock_Entry
    template_name = 'bipApp/report.html'
    context_object_name = 'snooples'

#def ReportView(request):
#   model = Time_Clock_Entry
#   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#   return render(request, "bipApp/report.html", {"snooples" : model, "days_of_week" : daysOfWeek})

class ListicleView(generic.ListView):
    template_name = 'bipApp/listicle.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'bipApp/detail.html'

class ResultsView(generic.DetailView):
   model = Question
   template_name = 'bipApp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bipApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bipApp:results', args=(question.id,)))

class ItemAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.is_authenticated():
            return Item.objects.none()

        qs = Item.objects.all()

        if self.q:
            qs = qs.filter(name__isstartswith=self.q)

        return self.q
