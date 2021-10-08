import boto3
from .ProcessZip import Extract
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import Developer, Locations, Properties, Status, zipdata, propertyImages, paymentPlan, priceRange, projectDetails, projectHighlights, projectAttachment
from .serializers import DeveloperSerialier, LocationsSerialier, paymentPlanSerialier, priceRangeSerialier, projectAttachmentSerializer, projectDetailsSerialier, projectHighlightsSerializer, propertyImagesSerialier, zipdataSerializer
from django.core import serializers
from openpyxl import load_workbook
import json
from django.http import HttpResponseForbidden
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import ast
from django.core.files.storage import default_storage
import pickle
from rest_framework.parsers import FileUploadParser
import random
from django.core.files.storage import FileSystemStorage


@api_view(['POST', ])
@csrf_exempt
def UploadFile(request):
    if request.method == "POST":
        print("req")
        zip_ser = zipdataSerializer(data=request.data)
        if zip_ser.is_valid():
        	zip_ser.save()
        	return Response(zip_ser.data, status=status.HTTP_201_CREATED)
        else:
        	return Response(zip_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        statuss = Status.objects.create(statuss="Processing")
        statuss.save()
        zipFIle = request.FILES["ufile"]
        respo = Extract(zipFIle)
        statuss.statuss = "Completed"
        statuss.save()
        return Response({"result": "success"}, status=status.HTTP_200_OK)
    else:
        return HttpResponseForbidden

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        statuss = Status.objects.create(statuss="Processing")
        statuss.save()
        #zipFIle = request.FILES["ufile"]
        respo = Extract(myfile)
        statuss.statuss = "Completed"
        statuss.save()
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')

@api_view(["GET", ])
def ViewDeveloper(request):
    developers = Developer.objects.all()
    developerSerialize = DeveloperSerialier(developers, many=True)
    return Response(developerSerialize.data, status=status.HTTP_200_OK)


@api_view(["GET", ])
def ViewLocations(request):
    developerId = request.GET.getlist('id')
    developer = Developer.objects.get(id=developerId[0])
    Location = Locations.objects.filter(developer=developer)
    locationSerialize = LocationsSerialier(Location, many=True)
    return Response(locationSerialize.data, status=status.HTTP_200_OK)


@api_view(["GET", ])
def ViewProperty(request):
    developerId = request.GET.getlist('did')
    locationId = request.GET.getlist('lid')
    developer = Developer.objects.get(id=developerId[0])
    location = Locations.objects.get(id=locationId[0])
    property = Properties.objects.filter(
        developer=developer, location=location)
    locationSerialize = LocationsSerialier(property, many=True)
    return Response(locationSerialize.data, status=status.HTTP_200_OK)


@api_view(["GET", ])
def ViewPropertyDetails(request):
    id = int(request.GET.getlist("pid")[0])
    properties = Properties.objects.get(id=id)

    project_details = projectDetails.objects.filter(property=properties)
    projectdetails_data = projectDetailsSerialier(project_details, many=True)

    priceRanges = priceRange.objects.filter(property=properties)
    pricerangeSerial = priceRangeSerialier(priceRanges, many=True)

    propertyimg = propertyImages.objects.filter(property=properties)
    propertyimgserl = propertyImagesSerialier(propertyimg, many=True)

    payplan = paymentPlan.objects.filter(property=properties)
    payplanser = paymentPlanSerialier(payplan, many=True)

    projectHigh = projectHighlights.objects.filter(property=properties)
    projectHighSer = projectHighlightsSerializer(projectHigh, many=True)

    projectattach = projectAttachment.objects.filter(property=properties)
    projectAttachSer = projectAttachmentSerializer(projectattach, many=True)

    data = {
        "images": propertyimgserl.data, "details": projectdetails_data.data, "price": pricerangeSerial.data, "paymentplan": payplanser.data, "highlights": projectHighSer.data, "attachments": projectAttachSer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST', ])
@csrf_exempt
def EditDeveloper(request):
    if request.method == "POST":
        received_json_data = (request.POST["name"])
        file = request.FILES["image"]
        developerObj = Developer.objects.get(name=received_json_data)
        media_storage = default_storage.save(file.name, file)
        file_url = "https://aajproperty.s3.ap-southeast-1.amazonaws.com/"+file.name
        developerObj.logo = file_url
        developerObj.save()
        return Response({"result": "success"}, status=status.HTTP_200_OK)
    else:
        return HttpResponseForbidden


@api_view(['POST', ])
@csrf_exempt
def Updatedetails(request):
    receive_Data = json.loads((request.body))
    print(receive_Data["pid"])
    prop = projectDetails.objects.get(property=int(receive_Data["pid"]))
    prop.projectdetails = json.dumps(receive_Data["propertyDetails"])


    prop.save()

    return Response({"result": "success"}, status=status.HTTP_200_OK)


@api_view(['POST', ])
@csrf_exempt
def UpdateImagesrank(request):
    receive_Data = json.loads((request.body))
    print(receive_Data["pid"])
    prop = propertyImages.objects.get(property=int(receive_Data["pid"]))
    prop.images = json.dumps(receive_Data["img"])
    prop.save()

    return Response({"result": "success"}, status=status.HTTP_200_OK)


@api_view(["GET", ])
def getStatus(request):
    try:
        statuss = Status.objects.all()[0]
        print("status", statuss.statuss)
        return Response({"result": statuss.statuss}, status=status.HTTP_200_OK)
    except:
        return Response({"result": "failer"}, status=status.HTTP_404_NOT_FOUND)


