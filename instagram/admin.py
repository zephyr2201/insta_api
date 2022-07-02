from django.contrib import admin

from instagram.models import (
    Content,
    Niche,
    Rubric,
    Text
)


class TextAdmin(admin.ModelAdmin):
    list_display = ('niche', 'rubric', 'content')


admin.site.register(Niche)
admin.site.register(Rubric)
admin.site.register(Content)
admin.site.register(Text, TextAdmin)
