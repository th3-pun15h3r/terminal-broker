from django import forms
from django.db.models.fields import CharField
from django.forms import widgets
from .models import SignUp


class SignUpForm(forms.ModelForm):
    full_name = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
    contact_no = forms.CharField(disabled=True)
    broker_email = forms.EmailField(disabled=True)
    dateof_issuance_of_brokercard = forms.CharField(disabled=True)
    name_of_the_establishment = forms.CharField(disabled=True)
    office_email = forms.EmailField(disabled=True)
    orn = forms.CharField(disabled=True)
    brn = forms.CharField(disabled=True)
    office_address = forms.CharField(disabled=True)
    dec_lisc = forms.CharField(disabled=True)
    agent_photo = forms.ImageField(disabled=True, required=False)
    company_logo = forms.ImageField(disabled=True, required=False)
    class Meta:
        model = SignUp
        fields = ['full_name', 'first_name', 'last_name', 'contact_no', 'broker_email', 'dateof_issuance_of_brokercard', 'brn', 'name_of_the_establishment', 'office_email', 'orn', 'office_address', 'dec_lisc', 'agent_photo', 'company_logo']


class EditSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SignUp
        fields = ['full_name', 'first_name', 'last_name', 'contact_no', 'broker_email', 'dateof_issuance_of_brokercard', 'brn', 'name_of_the_establishment', 'office_email', 'orn', 'office_address', 'dec_lisc', 'agent_photo', 'company_logo', 'password', 'confirm_password']


class EmailForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['broker_email']


class OtpForm(forms.Form):
    otp = forms.CharField(label='Enter Otp', max_length=100)
