import datetime

from django import forms
from student.models import Citizenship, CertificateType


class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.name

class StudentForm(forms.Form):
    sex = forms.CharField(label=u'Пол',max_length = 10)
    citizenship = NameModelChoiceField(label = u'Гражданство',queryset = Citizenship.objects.order_by('-name'),initial = Citizenship.objects.get(id=1))
    doc  = forms.CharField(label=u'Документ',max_length = 50)
    student_document_type = NameModelChoiceField(label=u'Документ студента',queryset=CertificateType.objects.order_by('-name'),initial = CertificateType.objects.get(id = 1))
    parent_document_type = NameModelChoiceField(label=u'Документ родителей',queryset=CertificateType.objects.order_by('-name'),initial = CertificateType.objects.get(id = 1))
    event_date = forms.DateTimeField(required=False,label=u'Дата добавления: ', initial=datetime.date.today,help_text=u'Введите дату')
    fio = forms.CharField(label=u'ФИО студента',max_length=60)

class ContractForm(forms.Form):
    number = forms.CharField(label=u'Номер договора',max_length=5)
    phone = forms.CharField(label=u'Телефон для контакта',max_length=7)
