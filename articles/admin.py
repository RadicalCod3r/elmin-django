from django.contrib import admin
from .models import Article, Comment

# Register your models here.

# class CommentsInline(admin.StackedInline):
#     model = Comment
#     extra = 0

class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentsInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)