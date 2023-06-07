from django.contrib import admin
from .models import Post, Author, Category, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('choice', 'title_post')
    list_display_links = ('choice', 'title_post')
    search_fields = ('choice', 'title_post')


admin.site.register(Post, NewsAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
