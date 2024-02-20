"""EmployeePayrollManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from employee import views
from django_otp.admin import OTPAdminSite 

  

admin.site.__class__ = OTPAdminSite 
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name='index'),
    path('register',views.register ,name='register'),
    path('SetPass/<int:pid>',views.SetPass ,name='SetPass'),
    path('EmpLogin',views.EmpLogin,name='EmpLogin'),
    path('EmpHome',views.EmpHome,name='EmpHome'),
    path('EmpProfile',views.EmpProfile,name='EmpProfile'),
    path('EmpPay',views.EmpPay,name='EmpPay'),
    path('Logout',views.Logout,name='Logout'),
    path('AdminLogin',views.AdminLogin,name='AdminLogin'),
    path('AdminHome',views.AdminHome,name='AdminHome'),
    path('AdminChangePass',views.AdminChangePass,name='AdminChangePass'),
    path('EmpExp',views.EmpExp,name='EmpExp'),
    path('EditExp',views.EditExp,name='EditExp'),
    path('EmpEdu',views.EmpEdu,name='EmpEdu'),
    path('EditEdu',views.EditEdu,name='EditEdu'),
    path('ChangePass',views.ChangePass,name='ChangePass'),
    path('AllEmployee',views.AllEmployee,name='AllEmployee'),
    path('DeleteEmployee/<int:pid>',views.DeleteEmployee,name='DeleteEmployee'),
    path('EditProfile/<int:pid>/<int:pid2>',views.EditProfile,name='EditProfile'),
    path('AllPayroll',views.AllPayroll,name='AllPayroll'),
    path('DeletePayroll/<int:pid>',views.DeletePayroll,name='DeletePayroll'),
    path('EditPayroll/<int:pid>',views.EditPayroll,name='EditPayroll'),
    path('AddPayroll',views.AddPayroll,name='AddPayroll'),
    path('GeneratePayroll',views.GeneratePayroll,name='GeneratePayroll'),
    path('AddEmployee',views.AddEmployee,name='AddEmployee'),
    path('validate',views.validateuser,name="validate_login"),
    path('validate_otp',views.validateOTP,name="validate_otp")

]
