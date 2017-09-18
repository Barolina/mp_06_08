from django.db import transaction
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from mp08.forms import PackageForm, MethodFormSet, MPForm, GeneralWorksForm, PersonForm
from .models import  *

class PackageMpListView(generic.ListView):
    model = PackageMp

    def get_context_data(self, **kwargs):
        context = super(PackageMpListView,self).get_context_data(**kwargs)
        context['method_mp'] = MethodMp.objects.all()
        return context

class MpListView(generic.ListView):
    model = PackageMp
    template_name = 'mp08/mp_list.html'
    context_object_name = 'mp_list'

class MpDetail(generic.DeleteView):
    model = PackageMp
    template_name = 'mp08/mp_detail.html'
    context_object_name = 'mp'

    def get_context_data(self, **kwargs):
        context = super(MpDetail, self).get_context_data(**kwargs)
        context['method'] = MethodMp.objects.filter(pk=self.kwargs.get('pk'))
        context['generalworks'] = GeneralWorks.objects.get(mp=self.kwargs['pk'])
        try:
            context['client'] = Person.objects.get(mp=self.kwargs['pk'])
        except:
            context['client'] = None
        return context

class MpAdd(CreateView):
    model = PackageMp
    form_class = PackageForm
    template_name = 'mp08/packagemp_form.html'
    context_object_name = 'mp'

    def get_success_url(self):
        return reverse('mp08:mp_list')

    def get_context_data(self, **kwargs):
        context = super(MpAdd, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:mp_add')
        return context

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super(MpAdd, self).form_valid(form)


class PackageCreate(CreateView):
    model = PackageMp
    form_class = PackageForm

    def get_success_url(self):
        return reverse('mp08:mp_detail',  kwargs={'pk':self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PackageCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:mp_add')
        return context

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super(PackageCreate, self).form_valid(form)

class GeneralWorksCreate(CreateView):
    model = GeneralWorks
    form_class = GeneralWorksForm
    template_name = 'mp08/packagemp_form.html'
    mp = object=None
    # context_object_name = 'generalwork'

    def get_success_url(self):
        return reverse('mp08:mp_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(GeneralWorksCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:generalworks_add',kwargs={'pk': self.kwargs['pk']})
        context['mp'] = PackageMp.objects.get(pk=self.kwargs['pk'])
        return context

    def dispatch(self, request, *args, **kwargs):
        self.mp = get_object_or_404(PackageMp, id=kwargs['pk'])
        return super(GeneralWorksCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.mp = self.mp
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'mp08/packagemp_form.html'
    mp = object=None
    # context_object_name = 'generalwork'

    def get_success_url(self):
        return reverse('mp08:mp_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(PersonCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:person_add',kwargs={'pk': self.kwargs['pk']})
        context['mp'] = PackageMp.objects.get(pk=self.kwargs['pk'])
        return context

    def dispatch(self, request, *args, **kwargs):
        self.mp = get_object_or_404(PackageMp, id=kwargs['pk'])
        return super(PersonCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.mp = self.mp
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView

class GeneralWorksCreateUpdate(UpdateView):
    model = GeneralWorks
    form_class = GeneralWorksForm
    template_name = 'mp08/packagemp_form.html'
    mp = object = None
    context_object_name = 'generalworks'

    def get_success_url(self):
        return reverse('mp08:mp_detail', kwargs={'pk': self.kwargs['m_pk']})


    def get_context_data(self, **kwargs):
        context = super(GeneralWorksCreateUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:generalworks_create_update', kwargs={'m_pk':self.kwargs['m_pk'],
                                                                               'pk': self.kwargs['pk']})
        context['mp'] = PackageMp.objects.get(pk=self.kwargs['m_pk'])
        context['generalworks'] = GeneralWorks.objects.get(pk=self.kwargs['pk'])
        return context

    # def get(self, request, *args, **kwargs):
    #     self.object = GeneralWorks.objects.get(pk=self.kwargs['g_pk'])
    #     return super(GeneralWorksCreateUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'mp08/packagemp_form.html'
    mp = object = None

    def get_success_url(self):
        return reverse('mp08:mp_detail', kwargs={'pk': self.kwargs['m_pk']})


    def get_context_data(self, **kwargs):
        context = super(PersonUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:person_update', kwargs={'m_pk':self.kwargs['m_pk'],
                                                                               'pk': self.kwargs['pk']})
        context['mp'] = PackageMp.objects.get(pk=self.kwargs['m_pk'])
        return context

        return super(PersonUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PackageUpdate(UpdateView):
    model = PackageMp
    template_name = 'mp08/packagemp_form.html'
    form_class = PackageForm
    context_object_name = 'mp'

    def get_success_url(self):
        return reverse('mp08:packages_list')

    def get_context_data(self, **kwargs):
        context = super(PackageUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:mp_update', kwargs={'pk':self.get_object().id})
        context['generalworks'] = GeneralWorks.objects.get(mp=self.kwargs['pk'])
        try:
            context['client'] = Person.objects.get(mp=self.kwargs['pk'])
        except:
            context['client'] = None
        return context


class PackageDetail(DetailView):
    model = PackageMp

class PackageDelete(DeleteView):
    model = PackageMp
    template_name = 'mp08/packagemp_delete.html'

    def get_success_url(self):
        return reverse('mp08:packages_list')

    def get_context_data(self, **kwargs):
        context = super(PackageDelete, self).get_context_data(**kwargs)
        context['action'] = reverse('mp08:package_delete', kwargs={'pk':self.get_object().id})
        return context

class PackageMethodUpdate(UpdateView):
    model = PackageMp
    fields = '__all__'

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PackageMethodUpdate,self).get_context_data(**kwargs)
        if self.request.POST:
            context['method'] = MethodFormSet(self.request.POST, instance = self.object)
        else:
            context['method'] = MethodFormSet(instance= self.object)

        return  context

    def form_valid(self, form):
        context = self.get_context_data()
        method = context['method']
        with transaction.atomic():
            self.object = form.save()

            if method.is_valid():
                method.instance = self.object
                method.save()
        return super(PackageMethodUpdate, self).form_valid(form)


class PackageMethodCreate(CreateView):
    model = MethodMp

    def get_success_url(self):
        return  reverse(self.get_object().self.get_absolut_url())