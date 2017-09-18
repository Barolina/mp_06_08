from django.db import models

# Create your models here.

class Citizenship(models.Model):
    name = models.CharField(max_length = 50,verbose_name= u'наименование')

class CertificateType(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'наименование')

class Student(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    sex = models.CharField(max_length=6,verbose_name=u"пол")
    citizenship = models.ForeignKey(Citizenship, verbose_name=u"гражданство")
    doc = models.CharField(max_length=240,verbose_name=u"doc")
    student_document_type = models.ForeignKey(CertificateType, related_name='student_document',verbose_name=u"документ студента")
    parent_document_type = models.ForeignKey(CertificateType, related_name='parent_document',verbose_name=u"документ родителей")

    def __str__(self):
        try:
            return  self.fiochange_set.latest('event_date').fio
        except FioChange.DoesNotExist:
            return  u'No name'

class Contract(models.Model):
    student = models.ForeignKey(Student,verbose_name=u'студента')
    number = models.CharField(max_length=24,verbose_name=u"Номер договора")
    student_home_phone = models.CharField(max_length=180, verbose_name=u"домашний телефон студента")

class FioChange(models.Model):
    id  = models.AutoField(primary_key=True, db_column='ID')
    event_date = models.DateField(verbose_name=u'дата создания фио',null=True,blank=True)
    student = models.ForeignKey(Student,verbose_name=u"студент")
    fio = models.CharField(max_length=120, verbose_name=u"ФИО")


    def __str__(self):
        return self.fio
