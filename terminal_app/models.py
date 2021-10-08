from django.db import models


class BuildingDetails(models.Model):
    project_name = models.CharField(max_length=500)
    unit_number = models.IntegerField()
    room_description = models.CharField(max_length=500)
    sizes = models.CharField(max_length=500)
    types = models.CharField(max_length=500)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.project_name


class PropertyData(models.Model):
    property_sold = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    property_type = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    price_per_sqft = models.CharField(max_length=100)
    built_up_area = models.CharField(max_length=100)
    bed = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class SignUp(models.Model):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    contact_no = models.CharField(max_length=500, null=True, blank=True)
    broker_email = models.EmailField(max_length=254, null=True, blank=True)
    dateof_issuance_of_brokercard = models.CharField(max_length=200, null=True, blank=True)
    brn = models.IntegerField()
    name_of_the_establishment = models.CharField(max_length=500, null=True, blank=True)
    office_email = models.EmailField(max_length=254, null=True, blank=True)
    orn = models.IntegerField(null=True, blank=True)
    office_address = models.CharField(max_length=700, null=True, blank=True)
    dec_lisc = models.IntegerField(null=True, blank=True)
    agent_photo = models.ImageField(upload_to ='agent_photo/',null=True, blank=True)
    company_logo = models.ImageField(upload_to ='company_logo/', null=True, blank=True)
    area_specialist = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    confirm_password = models.CharField(max_length=50, blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
         return str(self.id)
