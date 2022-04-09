from django.contrib import admin
from .models import Events, Gallery


def to_draft(modeladmin, request, queryset):
    for obj in queryset:
        obj.status = "draft"
        obj.save()


def to_published(modeladmin, request, queryset):
    for obj in queryset:
        obj.status = "published"
        obj.save()


class GalleryInLine(admin.TabularInline):
    model = Gallery


@admin.register(Events)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish', 'status')
    actions = [to_draft, to_published]
    inlines = [
        GalleryInLine
    ]