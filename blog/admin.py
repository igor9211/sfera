from django.contrib import admin
from .models import Post, Main, Child


def to_draft(modeladmin, request, queryset):
    for obj in queryset:
        obj.status = "draft"
        obj.save()


def to_published(modeladmin, request, queryset):
    for obj in queryset:
        obj.status = "published"
        obj.save()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    actions = [to_draft, to_published]


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Child)
class Child(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)