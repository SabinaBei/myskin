from django.contrib import admin
from shop.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     # prepopulated_fields = {'slug': ('name',)}
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'available']
#     list_filter = ['available']
#     list_editable = ['price', 'available']
#     # prepopulated_fields = {'slug': ('name',)}