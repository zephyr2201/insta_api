from django.contrib import admin

from instagram.models import (
    Content,
    Niche,
    Post,
    Rubric,
    Text,
    PostImage
)


class TextAdmin(admin.ModelAdmin):
    list_display = ('level', 'niche', 'rubric', 'content')
    list_filter = ('level', 'niche', 'rubric', 'content')


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('niche', 'rubric', 'content')
    list_filter = ('niche', 'rubric', 'content')


admin.site.register(Niche)
admin.site.register(Post)
admin.site.register(Rubric)
admin.site.register(Content)
admin.site.register(Text, TextAdmin)
admin.site.register(PostImage, PostImageAdmin)
