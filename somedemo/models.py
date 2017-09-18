# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse, reverse_lazy


class Categoty(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return  self.title

    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('categoty_detail', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse_lazy('test_categoty', kwargs={'pk': self.pk})


class SimplePage(models.Model):
    title = models.CharField(max_length=16)
    in_menu = models.BooleanField(default=True)
    order = models.SmallIntegerField()
    categoty  = models.ForeignKey(Categoty, default=True, null=True)
    # history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        return reverse_lazy('test_page', kwargs={'pk': self.pk})


class Books(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return  self.title


# from sitetree.models import TreeItemBase, TreeBase

#
# class MyTree(TreeBase):
#     """This is your custom tree model.
#     And here you add `my_tree_field` to all fields existing in `TreeBase`.
#
#     """
#     my_tree_field = models.CharField('My tree field', max_length=50, null=True, blank=True)
#
#
# class MyTreeItem(TreeItemBase):
#     """And that's a tree item model with additional `css_class` field."""
#     css_class = models.CharField('Tree item CSS class', max_length=50)