from django.contrib import admin

from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
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
        'description',
    )

    fieldsets = (
        ('project item', {
            'fields': (
                'title',
                'description',
                'url',
                'kind_of_project'
            ),
        }),
    )
