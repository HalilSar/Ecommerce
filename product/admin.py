from django.contrib import admin
from .models import Product,Category,Images
from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5 # Beş alan oluştur.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter=['status']
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','image_tag','amount','status')
    list_filter=['status','category']
    inlines = [ProductImageInline]
    readonly_fields = ('image_tag',)
# Register your models here.
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title','product')
    list_filter=['title','product']



class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin2)
admin.site.register(Images,ImagesAdmin)