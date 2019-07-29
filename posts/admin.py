from django.contrib import admin
from posts.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'photo')
    list_editable = ('title', 'photo')
    search_fields = (
        'title', 'profile__user__username', 'profile__user__email',
        'profile__user__first_name', 'profile__user__last_name',
    )
    list_filter = (
        'created', 'modified',
    )
    fieldsets = (
        ('Post', {
            'fields': (
                ('title',),
                ('photo',),
            ),
        }),
        ('Profile', {
            'fields': (
                ('profile',),
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )
    readonly_fields = ('created', 'modified')
