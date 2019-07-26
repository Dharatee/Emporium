from django.contrib import admin
from .models import first
# Register your models here.

class firstAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["name", "submission"]}),
        ("Content", {"fields": ["address"]})
    ]
 
admin.site.register(first, firstAdmin)
