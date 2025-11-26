from django import forms
from userapp.models import CustomUser,EmployeeModel

class UserRegistration(forms.ModelForm):

    class Meta:

      model = CustomUser

      fields = ["username","password","email","mobile_number"]

class LoginForm(forms.Form):
        
        username = forms.CharField(max_length=30)

        password = forms.CharField(max_length=30)

class EmployeeForm(forms.ModelForm):

    class Meta:

        model = EmployeeModel

        fields = ["name", "base_salary", "bonus", "tax"]


    