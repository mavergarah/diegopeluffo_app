from django.contrib import admin

from .models import Project, ThesisAdvisory, Collaborations, Teaching

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

@admin.register(ThesisAdvisory)
class ThesisAdmin(admin.ModelAdmin):
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
        'url',
    )

    fieldsets = (
        ('project item', {
            'fields': (
                'title',
                'url',
                'authors',
                'kind_of_thesis'
            ),
        }),
    )

@admin.register(Collaborations)
class CollaborationsAdmin(admin.ModelAdmin):
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
        'url',
    )

    fieldsets = (
        ('project item', {
            'fields': (
                'title',
                'url',
            ),
        }),
    )

@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
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
                'url',
                'description'
            ),
        }),
    )
