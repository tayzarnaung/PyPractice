from django.contrib import admin

from .models import Offer, Product
# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', )


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)


