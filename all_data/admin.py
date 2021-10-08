from django.contrib import admin
from .models import Properties, paymentPlan, priceRange, projectAttachment, projectDetails, projectHighlights, propertyImages, zipdata, Locations, Developer

admin.site.register(zipdata)
admin.site.register(Locations)
admin.site.register(Developer)

admin.site.register(Properties)
admin.site.register(projectHighlights)
admin.site.register(projectAttachment)
admin.site.register(projectDetails)
admin.site.register(propertyImages)
admin.site.register(paymentPlan)
admin.site.register(priceRange)

# admin.site.register(PropertyData)
