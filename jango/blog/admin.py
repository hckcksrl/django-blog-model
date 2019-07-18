from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'date_posted',
        'author'
    )
    list_display_links = (
        'title',
        'author'
    )

# Register your models here.
