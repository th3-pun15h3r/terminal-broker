from django.contrib import admin
from django.db import models
from .models import BuildingDetails, PropertyData, SignUp

# admin.site.register(PropertyData)
@admin.register(PropertyData)
class ProjectDataAdmin(admin.ModelAdmin):
    list_display = ['property_sold', 'location', 'property_type', 'price', 'price_per_sqft', 'built_up_area', 'bed']
    list_filter = ('property_type', 'bed')
    search_fields = ['property_sold', 'location', 'property_type', 'price', 'price_per_sqft', 'built_up_area', 'bed']

    fieldsets = (
        (None, {
            'fields': ('property_sold', 'location')
        }),
        ('Description', {
            'fields': ('property_type', 'price', 'price_per_sqft', 'built_up_area', 'bed')
        }),
    )

@admin.register(BuildingDetails)
class BuildingDetailsAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'unit_number', 'room_description', 'sizes', 'types', 'location']
    list_filter = ('project_name', 'unit_number')
    search_fields = ['project_name', 'unit_number', 'room_description', 'sizes', 'types', 'location']

    fieldsets = (
        (None, {
            'fields': ('project_name', 'unit_number')
        }),
        ('Description', {
            'fields': ('room_description', 'sizes', 'types', 'location')
        }),
    )

admin.site.register(SignUp)
