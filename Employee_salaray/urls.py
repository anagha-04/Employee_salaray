"""
URL configuration for Employee_salaray project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from userapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('create/',add_employee.as_view(),name="create"),
    path('edit/<int:pk>',EmployeeEditView.as_view(),name="edit"),
    path('list/',EmployeeListView.as_view(),name="list"),
    path('delete/<int:pk>',deleteView.as_view(),name="delete"),
]
