from django.contrib import admin

from .models import PersonalInfo

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
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
        'city',
        'profile',
        'phone',
        'email'
    )

    fieldsets = (
        ('personal item', {
            'fields': (
                'city',
                'profile',
                'phone',
                'email',
                'website',
                'profile_photo',
                'researchgate_url',
                'linkedin_url',
                'twitter_url',
                'facebook_url'
            ),
        }),
    )
