from django.contrib import admin
#ochrona przed atakami gdy np. dane pochodza od userow i
# #nieraz moga wrzucic jakeigos JS ktory moze spowodowac konflikt z panelem admina albo ataki xss
from django.utils.html import format_html
from .models import Idea, Vote

# # Register your models here.
# admin.site.register(Idea, )
# admin.site.register(Vote)

class VoteInLine(admin.StackedInline):
    model = Vote

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title','status','show_url']
    list_filter = ['status']
    inlines = [
        VoteInLine
    ]

    def show_url(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a href="{obj.youtube_url}">{obj.youtube_url}</a>')
        else:
            return ''

    show_url.short_description = 'Link'

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']



