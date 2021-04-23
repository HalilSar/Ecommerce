from django.contrib import admin
from .models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','productname','created_date','category')
    list_display_links = ('id','productname')
    list_filter = ('created_date',)
    search_fields = ('productname','description')
    list_per_page = 20
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','categoryname')
# Register your models here.

# Register your models here.
admin.site.register(Product,ProductAdmin)
# admin.site.register(ProductAdmin)
admin.site.register(Category,CategoryAdmin)
