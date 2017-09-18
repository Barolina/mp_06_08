from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from student.forms import StudentForm, ContractForm
from formtools.wizard.views import SessionWizardView

from student.models import Student, FioChange, Contract

FORMS = [
    ("student",StudentForm),
    ("contract" , ContractForm)
]

TEMPLATES = {
    "student"   :   "student/student.html",
    "contract"  :   "student/contract.html"
}
class AddStudentWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super(AddStudentWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'contract':
            context.update({'ok': 'True'})
        return context

    def done(self, form_list, **kwargs):
        student_form = StudentForm(self.form_list["student"])
        contract_form = ContractForm(self.form_list['contract'])
        s = Student.objects.create(
            sex = 'fsd',
            citizenship_id = 1,
            doc = 'sdasd',
            student_document_type_id = 1,
            parent_document_type_id =3

        )
        # s = Student.objects.create(
        #     sex = student_form.declared_fields['sex'],
        #     citizenship = student_form.declared_fields['citizenship'],
        #     doc = student_form.declared_fields['doc'],
        #     # student_document_type = student_form.declared_fields['student_document_type'],
        #     # parent_document_type = student_form.declared_fields['parent_document_type']
        # )
        f = FioChange.objects.create(
            student = s,
            event_date = student_form['event_date'],
            fio = student_form['fio']
        )
        c = Contract.objects.create(
            student = s,
            number = contract_form.declared_fields['number'],
            student_home_phone = contract_form.declared_fields['phone']
        )
        return HttpResponseRedirect(reverse('liststudent'))

class StudentsView(TemplateView):
    template_name = "student/list.html"

    def get_context_data(self, **kwargs):
        context =  super(StudentsView, self).get_context_data(**kwargs)
        context.update({
            'students'  :   Student.objects.all()
            })
        return context
