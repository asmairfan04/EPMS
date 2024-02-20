from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grade(models.Model):
    position=models.CharField(max_length=100)
    basic=models.PositiveIntegerField(default=0)
    DA=models.PositiveIntegerField(default=0)
    HRA=models.PositiveIntegerField(default=0)
    medical=models.PositiveIntegerField(default=0)
    transport=models.PositiveIntegerField(default=0)
    reimbursement=models.PositiveIntegerField(default=0)
    pf=models.PositiveIntegerField(default=0)
    esi=models.PositiveIntegerField(default=0)
    pt=models.PositiveIntegerField(default=0)
    tds=models.PositiveIntegerField(default=0)
    lwf=models.PositiveIntegerField(default=0)
 
    def __str__(self):
        return self.position


class EmpDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    middlename=models.CharField(max_length=50,null=True)
    empID=models.CharField(max_length=50)
    department=models.CharField(max_length=122,null=True)
    # grade_cl=models.ForeignKey(Grade,on_delete=models.CASCADE,related_name='grade_cl',default='1')
    # designation=models.ForeignKey(Grade,on_delete=models.CASCADE,related_name='designation')
    designation=models.CharField(max_length=122,null=True)
    contact=models.CharField(max_length=13,null=True)
    gender=models.CharField(max_length=50,null=True)
    joiningDate=models.DateField(null=True)
    dob=models.DateField(null=True)
    address=models.CharField(max_length=150,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    zip=models.CharField(max_length=15,null=True)

    # def save(self,*args,**kwargs):
    #     self.designation=(self.grade_cl.position)
    #     return super().save(*args,**kwargs)



    def __str__(self):
        return self.user.first_name


class EmpEducation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pgCourse=models.CharField(max_length=100,null=True)
    pgClg=models.CharField(max_length=200,null=True)
    pgYOP=models.CharField(max_length=10,null=True)
    pgPercentage=models.CharField(max_length=10,null=True)
    gradCourse=models.CharField(max_length=100,null=True)
    gradClg=models.CharField(max_length=200,null=True)
    gradYOP=models.CharField(max_length=10,null=True)
    gradPercentage=models.CharField(max_length=10,null=True)
    sscSchool=models.CharField(max_length=200,null=True)
    sscYOP=models.CharField(max_length=10,null=True)
    sscPercentage=models.CharField(max_length=10,null=True)
    hscSchool=models.CharField(max_length=200,null=True)
    hscYOP=models.CharField(max_length=10,null=True)
    hscPercentage=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.first_name

class EmpExperience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company1Name=models.CharField(max_length=100,null=True)
    company1Desig=models.CharField(max_length=100,null=True)
    company1Salary=models.CharField(max_length=100,null=True)
    company1Duration=models.CharField(max_length=100,null=True)
    company2Name=models.CharField(max_length=100,null=True)
    company2Desig=models.CharField(max_length=100,null=True)
    company2Salary=models.CharField(max_length=100,null=True)
    company2Duration=models.CharField(max_length=100,null=True)
    company3Name=models.CharField(max_length=100,null=True)
    company3Desig=models.CharField(max_length=100,null=True)
    company3Salary=models.CharField(max_length=100,null=True)
    company3Duration=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.first_name



class EmpPayroll(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    # grade_class=models.ForeignKey(Grade,on_delete=models.CASCADE,related_name='grade_class',default='1')
    basic=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    DA=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    HRA=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    medical=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    transport=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    reimbursement=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    pf=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    esi=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    pt=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    tds=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    lwf=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    tot_pay=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    tot_ded=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    net_pay=models.DecimalField(default=0,max_digits=10,decimal_places=2)


    # def save(self,*args,**kwargs):
    #     self.basic=(self.grade_class.basic)
    #     self.DA=(self.grade_class.basic*self.grade_class.DA/100)
    #     self.HRA=(self.grade_class.basic*self.grade_class.HRA/100)
    #     self.medical=(self.grade_class.medical)
    #     self.transport=(self.grade_class.transport)
    #     self.reimbursement=(self.grade_class.reimbursement)
    #     self.pf=(self.grade_class.basic*self.grade_class.pf/100)
    #     self.esi=(self.grade_class.basic*self.grade_class.esi/100)
    #     self.pt=(self.grade_class.basic*self.grade_class.pt/100)
    #     self.tds=(self.grade_class.basic*self.grade_class.tds/100)
    #     self.lwf=(self.grade_class.basic*self.grade_class.lwf/100)
    #     return super().save(*args,**kwargs)


    def __str__(self):
        return self.user.first_name


