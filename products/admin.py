from django.contrib import admin

from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'comment', 'stars', 'active', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'comment', 'stars', 'active', ]
