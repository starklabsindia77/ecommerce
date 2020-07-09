from django.contrib import admin
from product.models import Product,ProductImage,Colors,Size,Brand

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model=Product

class ProductImageAdmin(admin.ModelAdmin):
    class Meta:
        model=ProductImage

class ColorsAdmin(admin.ModelAdmin):
    class Meta:
        model=Colors
        
class SizeAdmin(admin.ModelAdmin):
    class Meta:
        model=Size
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)
admin.site.register(Colors,ColorsAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Brand)