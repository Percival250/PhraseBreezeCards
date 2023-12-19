from django.contrib import admin
from .models import Set, Card, SetCategory


admin.site.register(SetCategory)


class CardInline(admin.TabularInline):
    model = Card
    extra = 1


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'category', 'cards_count', 'downloads', 'is_published')
    list_display_links = ('id', 'name')
    ordering = ['id', 'is_published', 'downloads']
    list_editable = ('is_published', 'category')
    inlines = [CardInline]
