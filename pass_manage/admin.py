from django.contrib import admin
from .models import PasswordEntry

# Register your models here.
@admin.register(PasswordEntry)
class PasswordEntryAdmin(admin.ModelAdmin):
    list_display = ('website_name', 'email', 'password', 'note')
    search_fields = ('website_name', 'email')