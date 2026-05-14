from django.utils import timezone

from django.contrib import admin
from django.contrib import messages

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_completed',
        'is_long_standing',
    )

    list_filter = (
        'is_completed',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )

    list_per_page = 5

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'created_at',
    )

    list_editable = (
        'is_completed',
    )

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'is_completed')
        }),
        ('Additional Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    actions = (
        'mark_completed',
        'mark_uncompleted',
    )

    def is_long_standing(self, obj):
        """
       Custom field: check if the task was created a year ago.
        """
        return timezone.now().year - obj.created_at.year > 1

    is_long_standing.short_description = 'Long-standing'
    is_long_standing.boolean = True

    @admin.action(description='✅ Mark selected tasks as completed')
    def mark_completed(self, request, queryset):
        count = queryset.update(is_completed=True)

        self.message_user(
            request,
            f'{count} tasks marked as completed.',
            messages.SUCCESS
        )

    @admin.action(description='❌ Mark selected tasks as not completed')
    def mark_uncompleted(self, request, queryset):
        count = queryset.update(is_completed=False)

        self.message_user(
            request,
            f'{count} tasks marked as not completed.',
            messages.SUCCESS
        )

admin.site.site_header = "Task Manager Admin"
admin.site.site_title = "Task Manager"
admin.site.index_title = "Administration"

