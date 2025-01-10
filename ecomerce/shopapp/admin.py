from django.contrib import admin
from.models import product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable =  ['price','stock','available']
    prepopulated_fields = {'slug': ('name','gender','product_type')}

admin.site.register(product,ProductAdmin)
