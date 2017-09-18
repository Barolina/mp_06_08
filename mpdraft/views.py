from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import *

class GeneralWorksList(generic.ListView):
    model = GeneralWorks
    template_name = 'mpdraft/general_works_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(GeneralWorksList,self).get_context_data(**kwargs)
    #     context['method_mp'] = MethodMp.objects.all()
    #     return context