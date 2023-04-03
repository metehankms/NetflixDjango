from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display=['id','filmismi', 'kategori']
    list_display_links=['id']
    list_filter=['kategori']
    search_fields=['filmismi','kategori__name']
    list_per_page=2
    list_editable=['filmismi']

# Register your models here.

admin.site.register(Movies,MovieAdmin)
admin.site.register(Kategori)

admin.site.register(Izlenenler)
