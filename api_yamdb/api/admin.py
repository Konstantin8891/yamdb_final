from django.contrib import admin

from reviews.models import Category, Genre, Title, Review, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category', 'get_genres')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'score', 'author', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'author', 'text')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
