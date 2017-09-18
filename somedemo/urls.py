# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    # url(r'(?P<pk>\d+)/$', PageView.as_view(), name='page_detail'),
    url(r'categoty/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='categoty_detail'),
    url(r'categoty/$',  CategoyList.as_view(), name='categoty_list'),
    # url(r'books/$', BookList.as_view(), name='books_list'),

    url(r'book/$', BooksList.as_view(), name='books-listing'),
    url(r'book/(?P<pk>\d+)/$', BooksDetail.as_view(), name='books-details'),
    url(r'book/add/$', BooksAdd.as_view(), name='books-add'),

    url(r'^test/$',  TestList.as_view(), name= 'test'),
    url(r'^test/cat/(?P<pk>\d+)/$',  CategotyView.as_view(), name= 'test_categoty'),
    url(r'^page/(?P<pk>\d+)/$',  PageView.as_view(), name= 'test_page'),

    url(r'^charter/(?P<pk>\d+)/$', CategotyCharterView.as_view(), name= 'charter'),
    url(r'^test/cat1/(?P<cat>\d+)/page/(?P<pk>\d+)/$',  CatPage.as_view(), name= 'test_cat_page'),

]

