from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import About, Inquiry


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    list_display = ('title',)
    summernote_fields = ('description',)


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    """
    List user inquiries and editable read fild in admin
    """
    list_display = ('name', 'email', 'read', 'created_on',)
    list_editable = ('read',)
    search_fields = ['name', 'email']
    list_filter = ('read', 'created_on',)
