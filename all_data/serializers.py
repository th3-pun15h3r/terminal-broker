from rest_framework import serializers
from .models import Developer, Locations, Properties, paymentPlan, priceRange, projectAttachment, projectDetails, projectHighlights, propertyImages, zipdata


class zipdataSerializer(serializers.ModelSerializer):

    class Meta:
        model = zipdata
        fields = '__all__'


class DeveloperSerialier(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


class LocationsSerialier(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class PropertiesSerialier(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'


class propertyImagesSerialier(serializers.ModelSerializer):
    class Meta:
        model = propertyImages
        fields = '__all__'


class paymentPlanSerialier(serializers.ModelSerializer):
    class Meta:
        model = paymentPlan
        fields = '__all__'


class priceRangeSerialier(serializers.ModelSerializer):
    class Meta:
        model = priceRange
        fields = '__all__'


class projectDetailsSerialier(serializers.ModelSerializer):
    class Meta:
        model = projectDetails
        fields = '__all__'


class projectHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectHighlights
        fields = '__all__'


class projectAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectAttachment
        fields = '__all__'
