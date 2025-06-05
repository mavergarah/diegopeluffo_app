from django.contrib import admin

from .models import JournalInfo, BookInfo, ThesesInfo

@admin.register(JournalInfo)
class JournalInfoAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = (
        'bibbase_url',
    )

    fieldsets = (
        ('personal item', {
            'fields': (
                'bibbase_url',
            ),
        }),
    )

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = (
        'title',
        'publishing'
    )

    fieldsets = (
        ('personal item', {
            'fields': (
                'title',
                'publishing',
                'authors',
                'isbn',
                'category',
                'book_url'
            ),
        }),
    )

@admin.register(ThesesInfo)
class ThesesInfoAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = (
        'title',
        'author'
    )

    fieldsets = (
        ('personal item', {
            'fields': (
                'title',
                'author',
                'category',
                'theses_url'
            ),
        }),
    )
