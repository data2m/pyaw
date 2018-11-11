from django.contrib import admin

from .models import Asset, AssetLink, Machine, Project

class AssetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'updated_at', 'identifier')

class AssetLinkAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'asset_parent', 'asset_child', 'link_type')

admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetLink, AssetLinkAdmin)
admin.site.register(Machine)
admin.site.register(Project)
