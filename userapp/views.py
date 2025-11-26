from django.shortcuts import render,redirect

from userapp.forms import UserRegistration,LoginForm,EmployeeForm

from userapp.models import CustomUser,EmployeeModel

from django.contrib.auth import authenticate,login,logout

from django.views.generic import View,CreateView

from django.urls import reverse_lazy

# Create your views here.

class RegisterView(View):

    def get(self,request):
         
         form = UserRegistration()

         return render(request,"register.html",{"form":form})
    
    def post(self,request):

        form = UserRegistration(request.POST)   

        if form.is_valid():

            print(form.cleaned_data)

            CustomUser.objects.create_user(username = form.cleaned_data.get("username"),
                                      email =form.cleaned_data.get("email"),
                                      mobile_number =form.cleaned_data.get("mobile_number"),
                                      password =form.cleaned_data.get("password"))
            
            return render(request,"register.html")
        
        return render(request,"register.html")
    
class LoginView(View):

    def get(self,request):

        form = LoginForm()

        return render(request,'login.html',{"form":form})
    
    def post(self,request):

        form = LoginForm(request.POST)

        if form.is_valid():

           username = request.POST.get('username')

           password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)

        if user:

            login(request,user)

            return redirect("register")
        
        return render(request,"login.html")
    
    
class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("register")    
  
class add_employee(View):

    def get(self, request):

        form = EmployeeForm()
        
        return render(request, 'emp.html', {'form': form})

    def post(self, request):

        form = EmployeeForm(request.POST)

        if form.is_valid():

            emp = form.save(commit=False)

          
            emp.net_salary = emp.base_salary + emp.bonus - emp.tax

            emp.save()

         
            return render(request, 'emp.html', {'form': EmployeeForm(), 'success': True})

    
        return render(request, 'emp.html', {'form': form})
    
class EmployeeEditView(View):

    def get(self, request, **kwargs):

        id = kwargs.get('pk')

        emp = EmployeeModel.objects.get(id=id)

        form = EmployeeForm(initial={
            "name": emp.name,
            "base_salary": emp.base_salary,
            "bonus": emp.bonus,
            "tax": emp.tax
        })
        return render(request, "emp_edit.html", {"form": form})

    def post(self, request, **kwargs):

        id = kwargs.get('pk')

        emp = EmployeeModel.objects.get(id=id)

        emp.name = request.POST.get("name")

        emp.base_salary = float(request.POST.get("base_salary"))

        emp.bonus = float(request.POST.get("bonus"))

        emp.tax = float(request.POST.get("tax"))

        emp.net_salary = emp.base_salary + emp.bonus - emp.tax

        emp.save()

        return render(request,"emp_edit.html")
    
class EmployeeListView(View):

    def get(self, request):

        employees = EmployeeModel.objects.all()

        return render(request, "employee_list.html", {"employees": employees})


# class deleteView(View):

#     def get(self, request, **kwargs):

#         id = kwargs.get('pk')

#         emp = EmployeeModel.objects.get(id = id)

#         emp.delete()

#         return render(request,'employee_list.html')

    
    


