from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from django import forms
from .widgets import DragAndDropWidget
from .models import Category, Car, CarImage, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'created_on',)
    search_fields = ['name']
    list_filter = ('created_on',)
    

class CarImageInlineForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = '__all__'
        widgets = {
            'image': DragAndDropWidget(),
        }


class CarImageInline(admin.StackedInline):
    model = CarImage
    form = CarImageInlineForm
    extra = 1


@admin.register(Car)
class CarAdmin(SummernoteModelAdmin):

    inlines = [CarImageInline]
    list_display = ('title', 'owner', 'category', 'approved', 'created_on',)
    list_editable = ('approved',)
    search_fields = ['title', 'owner', 'model', 'brand', 'category']
    list_filter = ('approved', 'created_on', 'category',)
    summernote_fields = ('description',)
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('user','car', 'created',)
    list_filter = ('created',)