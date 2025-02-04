from django.contrib import admin
from . models import ClothingProduct , Bag , Accessory
# Register your models here.
@admin.register(ClothingProduct)
@admin.register(Bag)

class clothingproductmodeladmin(admin.ModelAdmin):
    list_display = ['id','title','size','price','description','category','color','image','created_at']
    

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'description', 'category', 'color', 'image', 'created_at') 
admin.site.register(Accessory, AccessoryAdmin)    