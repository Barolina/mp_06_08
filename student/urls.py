
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from material.frontend import urls as frontend_urls

from student.views import AddStudentWizard, FORMS, StudentsView

urlpatterns = [
    url(r'^addstudent/$', AddStudentWizard.as_view(FORMS), name='addstudent'),
    url(r'', StudentsView.as_view(), name='liststudent'),

]

