from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *
urlpatterns = [
    url(r'list/$', PackageMpListView.as_view(), name='packages_list'),
    # url(r'add/$', PackageCreate.as_view(), name='package_add'),
    url(r'delete/(?P<pk>\d+)$', PackageDelete.as_view(), name='package_delete'),

    # url(r'(?P<pk>[\d-]+)/*$', PackageDetail.as_view(), name='package_detail'),
    # url(r'edit/(?P<pk>\d+)$', PackageUpdate.as_view(), name='package_update'),
    url(r'edit/(?P<pk>\d+)/method$', PackageMethodUpdate.as_view(), name='package_method_update'),
    url(r'edit/(?P<pk>\d+)/method/add$', PackageMethodCreate.as_view(), name='methodmp_add'),


    url(r'mp/$', MpListView.as_view(), name='mp_list'),
    url(r'mp/add/$', PackageCreate.as_view(), name='mp_add'),
    url(r'mp/(?P<pk>[\d-]+)/*$', MpDetail.as_view(), name='mp_detail'),
    url(r'mp/(?P<pk>\d+)/edit/$', PackageUpdate.as_view(), name='mp_update'),

    # кадастровые работы
    url(r'mp/(?P<pk>\w+)/generalworks$', GeneralWorksCreate.as_view(), name='generalworks_add'),
    url(r'mp/(?P<m_pk>\w+)/generalworks/(?P<pk>\w+)/edit/$', GeneralWorksCreateUpdate.as_view(), name='generalworks_create_update'),

    url(r'mp/(?P<pk>\w+)/person$', PersonCreate.as_view(), name='person_add'),
    url(r'mp/(?P<m_pk>\w+)/person/(?P<pk>\w+)$', PersonUpdate.as_view(), name='person_update'),

]

# urlpatterns += staticfiles_urlpatterns()