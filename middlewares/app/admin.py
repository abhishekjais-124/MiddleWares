from django.contrib import admin
from app.models import Entity

# Register your models here.

class EntityAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Entity, EntityAdmin )