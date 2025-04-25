from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('description',)