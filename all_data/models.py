from os import name
from django.db import models
from django.db.models import JSONField


class zipdata(models.Model):
    root = models.TextField()
    data = models.TextField()
    name = models.TextField()
    file = models.FileField(blank=True, null=True)


class Developer(models.Model):
    name = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return self.name


class Locations(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Properties(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class propertyImages(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    images = models.TextField()

    def __str__(self):
        return self.property.name


class paymentPlan(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    paymentplan = models.TextField()

    def __str__(self):
        return self.property.name


class priceRange(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    pricerange = models.TextField()

    def __str__(self):
        return self.property.name


class projectDetails(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    projectdetails = models.TextField()

    def __str__(self):
        return self.property.name


class projectHighlights(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    projecthighlights = models.TextField()

    def __str__(self):
        return self.property.name


class projectAttachment(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    attachment = models.TextField()

    def __str__(self):
        return self.property.name


class Status(models.Model):
    statuss = models.TextField()
