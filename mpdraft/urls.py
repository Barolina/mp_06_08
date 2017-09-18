from django.conf.urls import url

from mp08.views import PackageMpListView

from .views import *
urlpatterns = [
    # url(r'list/$', PackageMpListView.as_view(), name='packages_list'),
    url(r'list/$', GeneralWorksList.as_view(), name='general_works_list'),
]