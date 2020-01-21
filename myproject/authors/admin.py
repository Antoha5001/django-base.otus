from django.contrib import admin
from .models import Author

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email_domen', 'level']
    list_display_links = ['id', 'first_name',]

    def email_domen(self, obj):
        return obj.email.partition('@')[2]


#admin.site.register(Author, AuthorAdmin)