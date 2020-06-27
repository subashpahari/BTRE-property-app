from django.contrib import admin
from realtors.models import Realtor

class RealotrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date' )
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25


# Register your models here.

admin.site.register(Realtor, RealotrAdmin)