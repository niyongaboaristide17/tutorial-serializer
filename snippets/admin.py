from django.contrib import admin

# Register your models here.
from .models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['created', 'title', 'code', 'linenos', 'language', 'style']
