from django.contrib import admin

from shop.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'price', 'is_public', 'created_at']
    list_filter = ['is_public', 'created_at']
