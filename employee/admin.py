from django.contrib import admin
from employee.models import *

# Register your models here.
admin.site.register(EmpDetail)
admin.site.register(EmpEducation)
admin.site.register(EmpExperience)
admin.site.register(EmpPayroll)
admin.site.register(Grade)