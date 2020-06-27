from django.contrib import admin
from listings.models import Listing

# creating custom adin page
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor' )
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'adderss', 'city', 'state', 'zipcode', 'price' )
    list_per_page = 25


# Register your models here.
admin.site.register(Listing, ListingAdmin)