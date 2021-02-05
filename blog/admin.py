from django.contrib import admin
from .models import Category, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "author", "published", "created", "post_categories")
    ordering = ("title", "published")
    search_fields = ("title", "content", "author__username", "categories__name")
    date_hierarchy = "published"
    list_filter = ("categories__name", "author__username")

    def post_categories(self, obj):
        return ", ".join(
            [category.name for category in obj.categories.all().order_by("name")]
        )


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

