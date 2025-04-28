from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from django import forms
from .widgets import DragAndDropWidget
from .models import Category, Car, CarImage, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Displays list of categories in admin.
    """
    list_display = ('name', 'created_on',)
    search_fields = ['name']
    list_filter = ('created_on',)


class CarImageInlineForm(forms.ModelForm):
    """
    Customize image upload form using
    custom :widdget:`widgets.DragAndDropWidget`.
    """
    class Meta:
        model = CarImage
        fields = '__all__'
        widgets = {
            'image': DragAndDropWidget(),
        }


class CarImageInline(admin.StackedInline):
    """
    Displays the car image form in car edit view as inline form.
    """
    model = CarImage
    form = CarImageInlineForm
    extra = 1


@admin.register(Car)
class CarAdmin(SummernoteModelAdmin):
    """
    Displays list of cars and its actions in Admin.
    """
    inlines = [CarImageInline]
    list_display = ('title', 'owner', 'category', 'approved', 'created_on',)
    list_editable = ('approved',)
    search_fields = ['title', 'owner', 'model', 'brand', 'category']
    list_filter = ('approved', 'created_on', 'category',)
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Displays list of the comments on the cars.
    """
    list_display = ('user', 'car', 'created',)
    list_filter = ('created',)
