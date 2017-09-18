from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.forms import inlineformset_factory
from django.urls import reverse_lazy

# from django_addanother.widgets import AddAnotherWidgetWrapper, AddAnotherEditSelectedWidgetWrapper

from .models import *
from .widgets import AddAnotherWidgetWrapper


def add_related_field_wrapper(form, col_name):
    rel_model = form.Meta.model
    rel = rel_model._meta.get_field(col_name).rel
    form.fields[col_name].widget =RelatedFieldWidgetWrapper(form.fields[col_name].widget, rel,admin.site,
                                                            can_add_related=True, can_change_related=True,
                                                            can_delete_related=True)

class MPForm(forms.ModelForm):
    method = forms.ModelChoiceField(queryset=MethodMp.objects.all())
    class Meta:
        model= PackageMp
        fields= ['method']

    def __init__(self, *args, **kwargs):
        super(MPForm, self).__init__(*args, **kwargs)
        self.fields['method'].queryset = MethodMp.objects.all()


class PackageForm(forms.ModelForm):

    method = forms.ModelChoiceField(queryset=MethodMp.objects.all(), required=False)
    owner = forms.ModelChoiceField(
        queryset=MethodMp.objects.all().order_by('name'),
        widget=AddAnotherWidgetWrapper(forms.Select(),MethodMp),
    )

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        # add_related_field_wrapper(self, 'offer')
        add_related_field_wrapper(self, 'method')

    class Meta:
        model= PackageMp
        fields = ['version_mp','method']
        # widgets = {
        #     'method': AddAnotherWidgetWrapper(
        #         forms.Select,
        #         reverse_lazy('mp_add'),
        #     ),}


class GeneralWorksForm(forms.ModelForm):
    class Meta:
        model= GeneralWorks
        exclude =['mp']

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        exclude=['mp']

class MethodForm(forms.ModelForm):
    class Meta:
        model = MethodMp
        exclude=()


MethodFormSet = inlineformset_factory(
    MethodMp,
    PackageMp,
    form=MethodForm,
    fields='__all__',
    extra=1
)