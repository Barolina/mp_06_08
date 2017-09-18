# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import *

# @admin.register(SimplePage)
# class SimplePageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'order', 'in_menu')


admin.site.register(Categoty)
admin.site.register(Books)

# admin.site.register(SimplePage, SimpleHistoryAdmin)
