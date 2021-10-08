from django.http.response import HttpResponseRedirect, JsonResponse
from terminal_app.models import BuildingDetails, PropertyData, SignUp
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
import json
import csv
from .forms import SignUpForm, EditSignUpForm, EmailForm, OtpForm
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.mail import send_mail
import math, random
import socket
from django.utils.datastructures import MultiValueDictKeyError
from all_data.models import Developer, Locations, Properties, zipdata, propertyImages, paymentPlan, priceRange, projectDetails, projectHighlights, projectAttachment
import ast

def buidingdetailsView(request):
    file = open('buildingdata1.csv', 'r')
    jsonfile = open('buildingdata1.json', 'w')
    fieldnames=("Project Name","Unit Number","ROOMS DESCRIPTION","Size","Type","Location")
    render = csv.DictReader(file)
    out = json.dumps([row for row in render])
    jsonfile.write(out)
    f=open('buildingdata1.json')
    newjson=json.load(f)
    for i in range(len(newjson)):
        c = BuildingDetails(project_name=newjson[i]["Project Name"],unit_number=newjson[i]["Unit Number"],room_description=newjson[i]["ROOMS DESCRIPTION"],sizes=newjson[i]["Size"],types=newjson[i]["Type "], location=newjson[i]["Location"])
        c.save()
    return HttpResponse("Inserted data successfully!")


def SignUpdetailsView(request):
    file = open('signupsheet.csv', 'r')
    jsonfile = open('signupsheet1.json', 'w')
    fieldnames=("Project Name","Unit Number","ROOMS DESCRIPTION","Size","Type","Location")
    render = csv.DictReader(file)
    out = json.dumps([row for row in render])
    jsonfile.write(out)
    jsonfile.close()
    f=open('signupsheet1.json')
    newjson=json.load(f)
    for i in range(len(newjson)):
        c = SignUp(full_name=newjson[i]["Full Name"],first_name=newjson[i]["First Name"],last_name=newjson[i]["Last Name"],
        contact_no=newjson[i]["Contact"],broker_email=newjson[i]["Broker Email"], dateof_issuance_of_brokercard=newjson[i]["Date of issunce of Brokercard"],
        brn=newjson[i]["BRN"], name_of_the_establishment=newjson[i]["Name of the Establishment"], office_email=newjson[i]["Office Email"],
        orn=newjson[i]["ORN"], office_address=newjson[i]["Office Address"], dec_lisc=newjson[i]["DEC Lisc"], agent_photo=newjson[i]["Agent Photo"],
        company_logo=newjson[i]["Company Logo"], area_specialist=newjson[i]["Area Specialists"])
        c.save()
    return HttpResponse("Inserted data successfully!")


def PropertyDataView(request):
    file = open('propertydata.csv', 'r')
    jsonfile = open('propertydata1.json', 'w')
    fieldnames=("Project Name","Unit Number","ROOMS DESCRIPTION","Size","Type","Location")
    render = csv.DictReader(file)
    out = json.dumps([row for row in render])
    jsonfile.write(out)
    f=open('propertydata1.json')
    newjson=json.load(f)
    for i in range(len(newjson)):
        c = PropertyData(property_sold=newjson[i]["Property SOLD"],location=newjson[i]["Location"],property_type=newjson[i]["Property Type"],price=newjson[i]["Price (AED)"],price_per_sqft=newjson[i]["Price/sqft (AED)"], built_up_area=newjson[i]["Built-up Area (sqft)"],bed=newjson[i]["Beds"])
        c.save()
    return HttpResponse("Inserted data successfully!")


def ipAddress(request):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def index(request):
    properties = Properties.objects.all()
    dev = Developer.objects.all()
    loc = Locations.objects.all()
    project_details = projectDetails.objects.all()
    list = []
    for values in project_details:
        p_properties = Properties.objects.get(name=values)
        project_detail = projectDetails.objects.get(property=p_properties)
        projectimg = propertyImages.objects.get(property=p_properties)
        pimg = ast.literal_eval(projectimg.images)

        projectdetails_data = json.loads(project_detail.projectdetails)
        Area_From = projectdetails_data['Area From']
        Starting_Price = projectdetails_data['Starting_Price']
        Bedrooms = projectdetails_data['Bedrooms']
        Type = projectdetails_data['Type']
        item_list = [key for (key, value) in pimg.items() if value == "0"]
        #print(item_list, "imglist")
        data = {
            "name": p_properties.name,
            "1": Area_From,
            "2": Starting_Price,
            "3": Bedrooms,
            "4": Type,
            "Location": p_properties.location,
            "Developer": p_properties.developer,
            "featureimage": item_list[0]

        }
        # json_data = json.dumps(data)
        list.append(data)
    trending = random.sample(list, 5)
    feature = random.sample(list, 5)
    fet = random.sample(list, 1)
    return render(request, 'home.html',{'project_details': list, "feature": feature,
                                          'properties': properties,
                                          'loc': loc,
                                          'dev': dev,
                                          "trending": trending,
                                          'fet':fet,})


def signup(request):
    if request.POST:
        brnNumber = request.POST.get('brn_number')
        brn_number = SignUp.objects.filter(brn=int(brnNumber))
        if brn_number:
            brn_number = get_object_or_404(SignUp, brn=int(brnNumber))
            form = SignUpForm(instance=brn_number)
            
            # broker email
            brokerEmail = form.initial['broker_email']
            email = brokerEmail.split('@')
            if len(email[0]) > 3:
                email_first = email[0].replace(email[0][len(email[0])-2:len(email[0])],"**")
            else:
                email_first = email[0].replace(email[0][len(email[0])-1:len(email[0])],"**")
            email_second = email[1][0].replace(email[1][0][len(email[1][0])-8:len(email[1][0])],"*****")
            form.initial['broker_email'] = email_first+"@"+email_second+".com"

            # office email
            officeEmail = form.initial['office_email']
            office_Email = officeEmail.split('@')
            if len(office_Email) > 3:
                email_office1 = office_Email[0].replace(office_Email[0][len(office_Email[0])-2:len(office_Email[0])],"**")
            else:
                email_office1 = office_Email[0].replace(office_Email[0][len(office_Email[0])-2:len(office_Email[0])],"**")   
            email_office2 = office_Email[1][0].replace(office_Email[1][0][len(office_Email[1][0])-8:len(office_Email[1][0])],"*****")
            form.initial['office_email'] = email_office1+"@"+email_office2+".com"

            # contact number
            contactNumber = form.initial['contact_no']
            contact = contactNumber.replace(contactNumber[7:], "********")
            form.initial['contact_no'] = contact

            form.initial['full_name'] = "**********"
            form.initial['first_name'] = "**********"
            form.initial['last_name'] = "***********"
            form.initial['dateof_issuance_of_brokercard'] = "***********"
            form.initial['name_of_the_establishment'] = "*************"
            form.initial['orn'] = '*********'
            form.initial['office_address'] = "***********"
            form.initial['dec_lisc'] = '************'
            form.initial['brn'] = '************'

            return render(request, 'signupform.html', {'form':form, 'pk':brn_number.id})
        else:
            messages.warning(request, 'Invalid BRN Number!')
            return render(request, 'signup_brn.html')         
    else:
        return render(request, 'signup_brn.html')


def edit_signup(request, pk):
    pk=pk
    email_validate = {'email':'','otp':''}
    request.session['email_validate']= email_validate
    if request.method == 'POST':
        if 'modal_button' in request.POST:
            try:
                obj = SignUp.objects.get(id=int(pk))
            except:
                obj = None
            if obj is not None:
                form = EditSignUpForm(instance=obj)
        if 'edit_signupData' in request.POST:
            brn = SignUp.objects.get(id=int(pk))
            form = EditSignUpForm(request.POST, request.FILES, instance=brn)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'Updated Successfully!')
                return redirect('index')
        else:
            return render(request, 'editsignup.html', {'form': form, 'pk':pk})
    
    return render(request, 'editsignup.html', {'form': form, 'pk':pk})


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def check_email(request):
    try:
        obj = SignUp.objects.get(broker_email=request.GET['email'])
    except:
        obj = None
    if obj is not None:
        email = obj.broker_email
        otp = generateOTP()
        htmlgen = '<p>Your OTP is <strong>'+otp+'</strong></p>'
        send_mail('OTP request',otp,'jainmanal98@gmail.com',[request.GET['email']], fail_silently=False, html_message=htmlgen)
        email_validate = {'email': email,'otp':otp}
        request.session['email_validate']= email_validate
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def check_otp(request):
    entered_otp = request.GET['otp']
    if entered_otp == request.session.get('email_validate')['otp']:
        signup_data = SignUp.objects.get(broker_email=request.session.get('email_validate')['email'])
        id = signup_data.id
        return JsonResponse({'status':1,'id':id})
    else:
        return JsonResponse({'status': 0})


def login_view(request):
    email = request.POST.get('login_email')
    password = request.POST.get('login_password')
    try:
        signup_data = SignUp.objects.get(broker_email=email)
    except:
        signup_data = None

    if signup_data is not None:
        if signup_data.broker_email == 'superadmin@gmail.com':
            if signup_data.password == 'superadmin':
                request.session['admin_login'] = signup_data.first_name
                return redirect('dashboard')
            else:
                return redirect('index')    
        if signup_data.password == password:
            if 'login_submit' in request.POST:
                request.session['login_email'] = email
                return redirect('index')

    return render(request, 'login.html')


def logout(request):
    del request.session['login_email']
    return redirect('index')


def dashboard(request):
    return render(request, 'dashboard.html')


def buildingdata(request):
    return render(request, 'Building.html')


def propertydata(request):
    return render(request, 'Property.html')


def signupdata(request):
    signup_data1 = SignUp.objects.all()
    dataset = []
    for x in signup_data1:
        val = {
            'id': x.id,
            'full_name': x.full_name,
            'brn': x.brn,
            'decLisc': x.dec_lisc,
            'company_name': x.name_of_the_establishment,
            'office_email': x.office_email
        }
        dataset.append(val)
    return render(request, 'Signups.html', {'dataset': dataset})


def admin_logout(request):
    del request.session['admin_login']
    return redirect('index')


def get_SignupDetails(request):
    if request.method == 'POST':
        if 'edit_signupdata' in request.POST:
            id = request.POST.get('formId-test')
            signup = SignUp.objects.get(id=id)
            signup.full_name = request.POST.get('fullName')
            signup.first_name = request.POST.get('firstName')
            signup.last_name = request.POST.get('lastName')
            signup.contact_no = request.POST.get('contactNumber')
            signup.broker_email = request.POST.get('BrokerEmail')
            signup.dateof_issuance_of_brokercard = request.POST.get('DateofIssuance')
            signup.brn = request.POST.get('Brn')
            signup.name_of_the_establishment = request.POST.get('NameofEstablishment')
            signup.office_email = request.POST.get('officeEmail')
            signup.orn = request.POST.get('Orn')
            signup.office_address = request.POST.get('officeAddress')
            signup.dec_lisc = request.POST.get('declisc')
            if request.FILES.get('agent_photo') is not None and request.FILES.get('company_logo') is not None:
                signup.agent_photo = request.FILES.get('agent_photo')
                signup.company_logo = request.FILES.get('company_logo')
            if request.FILES.get('agent_photo') is not None:
                signup.agent_photo = request.FILES.get('agent_photo')
            if request.FILES.get('company_logo') is not None:
                signup.company_logo = request.FILES.get('company_logo')
            signup.area_specialist = request.POST.get('areaSpecialist')
            signup.approved = request.POST.get('approved')
            if signup.approved == 'on':
                signup.approved = True
            else:
                signup.approved = False

            signup.save()
            return redirect('dashboard')
    else:
        id = request.GET.get('id')
        data = SignUp.objects.get(id=id)
        if data.approved:
            approve = 'True'
        else:
            approve = 'False'
        if data.agent_photo:
            agent_photo_url = data.agent_photo.url
        else:
            agent_photo_url = 'None'
        if data.company_logo:
            company_photo_url = data.company_logo.url
        else:
            company_photo_url = 'None'
        json_data = {
            'id': data.id,
            'full_name': data.full_name,
            'first_name': data.first_name,
            'last_name': data.last_name,
            'contact_no': data.contact_no,
            'broker_email': data.broker_email,
            'dateof_issuance_of_brokercard': data.dateof_issuance_of_brokercard,
            'brn': data.brn,
            'name_of_the_establishment': data.name_of_the_establishment,
            'office_email': data.office_email,
            'orn': data.orn,
            'office_address': data.office_address,
            'dec_lisc': data.dec_lisc,
            'agent_photo': agent_photo_url,
            'company_logo': company_photo_url,
            'area_specialist': data.area_specialist,
            'approved': approve
        }
        return JsonResponse(json_data)


def getCompanyDetails(request):
    id = request.GET.get('id')
    c_name = SignUp.objects.get(id=id)
    company_name = c_name.name_of_the_establishment

    data = SignUp.objects.filter(name_of_the_establishment=company_name)
    if data:
        dataset = []
        for x in data:
            val = {
                'full_name': x.full_name,
                'contact_no': x.contact_no,
                'broker_email': x.broker_email,
                'dateof_issuance_of_brokercard': x.dateof_issuance_of_brokercard,
                'brn': x.brn,
                'office_email': x.office_email,
                'orn': x.orn,
                'office_address': x.office_address,
                'dec_lisc': x.dec_lisc
            }
            dataset.append(val)
        return JsonResponse({'dataset':dataset})
