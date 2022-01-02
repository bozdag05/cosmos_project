from django.contrib import admin
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Reports, Author

class ReportsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_date',  'is_published']
    list_display_links = ('id', 'title')
    search_fields = ['title', 'author']



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'speciality', 'get_photo']
    list_display_links = ('id', 'speciality', 'first_name', 'last_name')
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'не установлено'

    get_photo.short_description = 'фото'

admin.site.register(Reports, ReportsAdmin)
admin.site.register(Author, AuthorAdmin)
