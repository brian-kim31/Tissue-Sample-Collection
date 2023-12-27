from django.contrib import admin
from .models import Collection, Sample

# Register your models here.

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'disease_term', 'title')

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection', 'user', 'donor_count', 'material_type', 'last_updated')
