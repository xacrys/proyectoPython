from django.contrib import admin
from .models import Page


class PagesConfig(admin.ModelAdmin):
    list_display = ("title", "order")


# Register your models here.
admin.site.register(Page, PagesConfig)
