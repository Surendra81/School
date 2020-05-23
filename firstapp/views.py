from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import School, Question, Choice
from django.shortcuts import get_object_or_404
from .forms import CreateSchool
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# class SchoolView(ListView):
#     model = School

#     template_name = 'firstapp/index.html'
        


#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a   context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['school_list'] = School.objects.all()
#         return context



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('firstapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)