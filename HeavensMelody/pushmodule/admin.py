from django.contrib import admin

from pushmodule.models import create

# Register your models here.

class createField(admin.ModelAdmin):
    list_display = ['id', 'title', 'time', 'username', 'short_description', 'short_lyrics',
                   'beat', 'short_story', 'photos', 'filter']
    class meta:
        model = create
admin.site.register(create, createField)