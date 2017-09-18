from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Citizenship)
admin.site.register(CertificateType)
admin.site.register(Student)
admin.site.register(Contract)
admin.site.register(FioChange)

