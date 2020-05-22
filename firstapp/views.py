from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import School
from django.shortcuts import get_object_or_404
from .forms import CreateSchool
from django.views.generic.edit import CreateView
# Create your views here.

class SchoolView(ListView):
    model = School

    template_name = 'firstapp/index.html'
        


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['school_list'] = School.objects.all()
        return context

class SchoolCreate(CreateView):
    model = School
    fields = '__all__'
    template_name = 'firstapp/create.html'
