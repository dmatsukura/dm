from django.contrib import admin
from . models import ContactProfile

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name', 'email', 'message')
    list_filter = ('id', 'timestamp', 'name', 'email', 'message')
    search_fields = ('timestamp', 'name', 'email', 'message')
    ordering = ('id', 'timestamp', 'name', 'email', 'message')
