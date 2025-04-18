from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from django.contrib import admin
from .models import Category, Car, CarImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'created_on',)
    search_fields = ['name']
    list_filter = ('created_on',)


class CarImageInline(admin.StackedInline):
    model = CarImage
    extra = 1
    readonly_fields = ['preview']

    class Media:
        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/min/dropzone.min.js',
            'js/custom_dropzone.js',
        ]
        css = {
            'all': [
                'https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/min/dropzone.min.css',
                'css/custom_dropzone.css',
            ]
        }

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 150px;" />', obj.image.url)
        return "No image"


@admin.register(Car)
class CarAdmin(SummernoteModelAdmin):

    inlines = [CarImageInline]
    list_display = ('title', 'owner', 'category', 'approved', 'created_on',)
    list_editable = ('approved',)
    search_fields = ['title', 'owner', 'model', 'brand', 'category']
    list_filter = ('approved', 'created_on', 'category',)
    summernote_fields = ('description',)