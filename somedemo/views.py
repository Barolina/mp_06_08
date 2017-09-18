# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, CreateView


from .models import *




class CategoyList(ListView):
    model = Categoty



class CategoryDetail(DetailView):
    template_name = 'somedemo/categoty_detail.html'
    model = Categoty


    def get_context_data(self, **kwargs):
        context = super(CategoryDetail,self).get_context_data(**kwargs)
        context['pages'] = SimplePage.objects.filter(pk=self.kwargs.get('pk'))
        return  context


class BookList(ListView):
    model = Categoty
    context_object_name = 'books_list'

class BooksList(ListView):
    template_name = 'somedemo/categoty_list.html'
    model = Books

class BooksDetail(DetailView):
    template_name = 'somedemo/categoty_detail.html'
    model = Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class BooksAdd(CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'somedemo/books_form.html'

    def get_success_url(self):
        return reverse('books-listing')


class TestList(ListView):
    model = Categoty
    template_name = 'test/test.html'
    context_object_name = 'categoty_list'

class CategotyView(DetailView):
    model = Categoty
    template_name = 'test/categoty_detail.html'
    context_object_name = 'categoty_page'

    def get_context_data(self, **kwargs):
        context = super(CategotyView,self).get_context_data(**kwargs)
        context['pages'] = SimplePage.objects.filter(pk=self.kwargs.get('pk'))
        return  context


class PageView(DetailView):
    model =  SimplePage
    template_name = 'test/page_detail.html'
    context_object_name = 'simple_page'


class CatPage(DetailView):
    model = Categoty
    template_name = 'test/page_detail.html'
    context_object_name = 'categoty_page'

    def get_queryset(self):
        return  self.model.objects.filter(pk=self.kwargs.get('cat'))

    def get_context_data(self, **kwargs):
        context = super(CatPage, self).get_context_data(**kwargs)
        context['pages'] = SimplePage.objects.filter(pk=self.kwargs.get('pk'))[0]
        return context

class CategotyCharterView(DetailView):
    model = Categoty
    template_name = 'test/charter.html'
    context_object_name = 'categoty_page'

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(CategotyCharterView,self).get_context_data(**kwargs)
        context['pages'] = SimplePage.objects.all()
        return  context

