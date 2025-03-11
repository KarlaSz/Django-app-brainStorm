from django.contrib import admin
from .models import Idea, Vote

# # Register your models here.
# admin.site.register(Idea, )
# admin.site.register(Vote)

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['status', 'title']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']



