from django.contrib import admin

from .models import *

#admin.site.register(Categories)
#admin.site.register(Orders)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'category', 'other_name', 'age', 'description', 'owner')
    list_display_links = ('id', 'date', 'category', 'other_name', 'age', 'description', 'owner')