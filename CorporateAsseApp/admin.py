from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Company),
admin.site.register(Employees),
admin.site.register(Role),
admin.site.register(Assets),

class AssetTrackAdmin(admin.ModelAdmin):
    search_fields = ('title', 'asset', 'employee')
    list_display = ('title', 'employee', 'condition_at_checkout','condition_at_return','checkout_at','returned_at')
admin.site.register(AssetTrack, AssetTrackAdmin),
