from django.contrib import admin

# Register your models here.

from yto_cmdb.models import cmdb,people,cabinet,idc,container
admin.site.register(cmdb)
admin.site.register(people)
admin.site.register(cabinet)
admin.site.register(idc)
admin.site.register(container)