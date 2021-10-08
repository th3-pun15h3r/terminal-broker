from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [

    path("uploadDeveloper/", views.simple_upload, name="uploads"),
    path("viewdeveloper/", views.ViewDeveloper, name="views"),
    path("viewLocations/", views.ViewLocations, name="views"),
    path("viewProperties/", views.ViewProperty, name="views"),
    path("viewpropertydetails/", views.ViewPropertyDetails, name="viewsp details"),
    path("editdeveloper/", views.EditDeveloper, name="edit developer"),
    path("updatedetails/", views.Updatedetails, name="updatedetails"),
    path("updateimages/", views.UpdateImagesrank, name="updateimages"),
    path("getStatus/", views.getStatus, name="status"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
