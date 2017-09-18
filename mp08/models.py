from django.db import models
import uuid

from django.urls import reverse
from django.views.generic import DetailView


class MethodMp(models.Model):
    name = models.CharField(max_length=255, verbose_name='описание метода')
    # package = models.ForeignKey('PackageMp', default=True, blank=True, null=True)
    class Meta:
        verbose_name = 'Метод образования'
        app_label= 'mp08'

    def __str__(self):
        return  self.name

# Create your models here.
class PackageMp(models.Model):
    guid = models.UUIDField( default=uuid.uuid4, editable=False)
    version_mp = models.CharField(max_length=255,  default='06',blank=False, null=False)
    method = models.ForeignKey(MethodMp, blank=True, null= True, related_name='package')

    class Meta:
        verbose_name = 'Проект'
        app_label = 'mp08'

    def __str__(self):
        return  str(self.id) + ' ' +self.version_mp+' '+str(self.guid)

    def get_absolute_url(self):
        return reverse('mp08:mp_detail', args=[str(self.pk)])

class GeneralWorks(models.Model):
    reason = models.CharField(max_length=255, default='06', blank=False, null=False)
    pupose = models.CharField(max_length=255, default='06', blank=False, null=False)
    n_doc = models.PositiveIntegerField(blank=True, null=True)
    mp = models.ForeignKey(PackageMp)

    class Meta:
        verbose_name = 'Общие сведения кадастровых  работ'
        app_label = 'mp08'

    def __str__(self):
        return self.reason +' '+self.pupose

    def get_absolute_url(self):
        return reverse('mp08:mp_detail', args=[str(self.pk)])

class Person(models.Model):
    fio = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    other = models.CharField(max_length=255, blank=True, null=True)
    snils = models.CharField(max_length=255)
    mp = models.ForeignKey(PackageMp)

    class Meta:
        verbose_name = 'Физтческое лицо'
        app_label = 'mp08'

    def __str__(self):
        return  self.fio + ' '+self.other