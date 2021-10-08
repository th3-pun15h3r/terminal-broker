"""terminal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from terminal_app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('build/', buidingdetailsView),
    # path('property/', PropertyDataView),
    # path('signupdata/', SignUpdetailsView),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('edit_signup/<pk>/', edit_signup, name='edit_signup'),
    # path('email_submit/', emailValidation, name='email_submit'),
    # path('otp_submit/', otpValidationView, name='otp_submit'),
    path('check_email/', check_email, name='check_email'),
    path('check_otp/', check_otp, name='check_otp'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('building/', buildingdata, name="building"),
    path('property/', propertydata, name="property"),
    path('Signups/', signupdata, name="signups"),
    path('admin_logout/', admin_logout, name="admin_logout"),
    path('get_SignupDetails/', get_SignupDetails, name="get_SignupDetails"),
    path('getCompanyDetails/', getCompanyDetails, name="getCompanyDetails"),
    path("api/", include("all_data.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)