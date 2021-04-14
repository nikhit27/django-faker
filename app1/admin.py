from django.contrib import admin

from .models import *
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'emailid', 'contactno')
    list_filter = ['name']
    search_fields = ('name', 'emailid', 'contactno')
    prepopulated_fields = {'emailid':('name',)}
    list_editable = ['emailid', ]
    #{'emailid',}  <-This can be used too
    # date_hierarchy = ['date when created',]
admin.site.register(person, PersonAdmin)
