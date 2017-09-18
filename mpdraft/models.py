import uuid

from django.db import models
from django.urls import reverse


class Draft_TypeMp(models.Model):
    '''
       справочник - типов межевых планов
    '''
    name = models.CharField(max_length=255,  default='Образование')
    class Meta:
        verbose_name='Тип межевого плана'

    def __str__(self):
        return  self.name


# Create your models here.
class Draft_Mp(models.Model):
    guid = models.UUIDField( default=uuid.uuid4, editable=False)
    version = models.CharField(max_length=255,  default='06',blank=False, null=False)
    method = models.ForeignKey(Draft_TypeMp, blank=True, null= True, related_name='type_mp')
    name_soft = models.CharField(max_length=255,  default='itt', blank=False, null=False)

    class Meta:
        verbose_name = 'Проект'
        app_label = 'mpdraft'

    def __str__(self):
        return  str(self.id) + ' ' +self.version_mp+' '+str(self.guid)

    # def get_absolute_url(self):
    #     return reverse('mpdraft:mp_detail', args=[str(self.pk)])

class PersonQualified(models.Model):
    family_name = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    poatronymic = models.CharField(max_length=255)

    class Meta:
        verbose_name= 'ФИО'
        app_label = 'mpdraft'

    def __str__(self):
        return  self.family_name+ ' '+ self.first_name

class Organization(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    adress = models.CharField(max_length=4000, blank=False, null=False)

    class Meta:
        verbose_name= 'Организаиця'

    def __str__(self):
        return  self.name

class AgreementCadWork(models.Model):
    '''
        mp_08
    '''
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=4000, blank=False, null=False)

    class Meta:
        verbose_name = 'Номер и дата заключения договора на выполнение кадастровых работ'
        app_label = 'mpdraft'

    def __str__(self):
        return  self.name


class Contractor(PersonQualified):
    snils = models.CharField(max_length=14, blank=False, null=False)
    engineerregistry_number = models.CharField(max_length=50, blank=False, null=False)
    telefon = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=4000, blank=False, null=False)
    email = models.CharField(max_length=4000, blank=False, null=False)
    organization = models.ForeignKey(Organization, default=True, null=True)
    draft_selfregulatory_organization = models.CharField(max_length=255, blank=False, null=False)
    draft_agreement_cadwork  = models.ForeignKey(AgreementCadWork)

    class Meta:
        verbose_name = 'Исполнитель'
        app_label = 'mpdraft'



class GeneralWorks(models.Model):
    reason = models.CharField(max_length=4000, blank=False, null=False)
    pupose = models.CharField(max_length=4000, blank=True, null=True)
    date_cadastral = models.DateField(blank=False, null=False)
    mp = models.ForeignKey(Draft_Mp)
    contractor  = models.ForeignKey(Contractor)

    class Meta:
        verbose_name = 'Общие сведения кадастровых  работ'
        app_label = 'mpdraft'

    def __str__(self):
        return self.reason + ' ' + self.mp.guid

    # def get_absolute_url(self):
    #     return reverse('mpdraft:mp_detail', args=[str(self.pk)])