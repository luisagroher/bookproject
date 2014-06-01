from django.contrib import admin
from django.contrib import admin

from models import Book, Chapter, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 0
    
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    inlines = [ChapterInline, CommentInline]

admin.site.register(Book, BookModelAdmin)

class CommentsModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentsModelAdmin)

class ChapterModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chapter, ChapterModelAdmin)
