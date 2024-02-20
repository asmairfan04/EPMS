from distutils.log import error
from turtle import position
from xmlrpc.client import Transport
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.models import User
from employee.models import EmpDetail, EmpEducation, EmpExperience,EmpPayroll, Grade
from django.contrib.auth import login,logout,authenticate
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import re 
from re import sub
import random
import qrcode
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders, message
import pandas as pd



from django.conf import settings
from django.core.mail import send_mail

otp=0
eid=""

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    error=""
    if request.method=="POST":
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        email=request.POST['email']
        empID=request.POST['EmpID']
        try:
            user=User.objects.get(username=empID)
            employee=EmpDetail.objects.get(user=user)
            if user.first_name==firstname and user.last_name==lastname and user.email==email and employee.middlename==middlename :
                error="Exists"
            else:
                error="Not Exist"

        except:
            error="Not Exist"


        
        # pwd=request.POST['pwd']
        # try:
        #     user= User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=pwd,username=empID)
        #     EmpDetail.objects.create(user=user,middlename=middlename,empID=empID)
        #     EmpExperience.objects.create(user=user)
        #     EmpEducation.objects.create(user=user)
        #     EmpPayroll.objects.create(user=user)
        #     error="NO"
        # except:
        #     error="YES"

    return render(request,"register.html",locals())


def SetPass(request,pid):
    error=""
    if request.method=="POST":
        pwd=request.POST['pwd']
        flag = 0
        while True:   
            if (len(pwd)<8): 
                flag = -1
                break
            elif not re.search("[a-z]", pwd): 
                flag = -1
                break
            elif not re.search("[A-Z]", pwd): 
                flag = -1
                break
            elif not re.search("[0-9]", pwd): 
                flag = -1
                break
            elif not re.search("[_@$]", pwd): 
                flag = -1
                break
            elif re.search("\s", pwd): 
                flag = -1
                break
            else: 
                flag = 0 
                break
        if flag==0:
            try:
                user=User.objects.get(username=pid)
                user.set_password(pwd)
                user.save()
                # subject = 'welcome to GFG world'
                # message = 'Hi, thank you for registering in geeksforgeeks.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email, ]
                # send_mail( subject, message, email_from, recipient_list )
                error="NO"

            except:
                error="YES"
        if flag==-1:
            error="Invalid Pass"
        
        

        # pwd=request.POST['pwd']
        # try:
        #     user= User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=pwd,username=empID)
        #     EmpDetail.objects.create(user=user,middlename=middlename,empID=empID)
        #     EmpExperience.objects.create(user=user)
        #     EmpEducation.objects.create(user=user)
        #     EmpPayroll.objects.create(user=user)
        #     error="NO"
        # except:
        #     error="YES"

    return render(request,"SetPass.html",locals())



def EmpLogin(request):
    # error=""
    # x=0
    # user=None
    # if request.method=='POST' and 'send_otp' in request.POST:
    #     empID=request.POST['EmpID']
    #     pwd=request.POST['pwd']
    #     user=authenticate(username=empID,password=pwd)
    #     # print(user)
    #     # print(int(user.username))
    #     # print(user.email)
    #     if user:
    #         x=random.randint(10000000,99999999)
    #         im=qrcode.make("OTP is "+str(x))
    #         t=str(user.get_username())
    #         im.save(r"employee/static/qr/"+t+".jpg")
    #         path="employee/static/qr/"+t+".jpg"

    #         # Define the HTML document
    #         html = '''
    #             <html>
    #                 <body>
    #                     <h1>Scan the QR code</h1>
    #                     <p>Enter the 8-digit OTP generated!</p>
    #                 </body>
    #             </html>
    #             '''

    #         # Define a function to attach files as MIMEApplication to the email
    #         ##############################################################
    #         def attach_file_to_email(email_message, filename):
    #             # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    #             with open(filename, "rb") as f:
    #                 file_attachment = MIMEApplication(f.read())
    #             # Add header/name to the attachments    
    #             file_attachment.add_header(
    #                 "Content-Disposition",
    #                 f"attachment; filename= {filename}",
    #             )
    #             # Attach the file to the message
    #             email_message.attach(file_attachment)
    #         ##############################################################    

    #         # Set up the email addresses and password. Please replace below with your email address and password
    #         email_from = 'epms.major@gmail.com'
    #         password = 'beqcpwbqikkegvtu'
    #         email_to = user.email

    #         # Generate today's date to be included in the email Subject
    #         date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    #         # Create a MIMEMultipart class, and set up the From, To, Subject fields
    #         email_message = MIMEMultipart()
    #         email_message['From'] = email_from
    #         email_message['To'] = email_to
    #         email_message['Subject'] = f'EPMS Validation - {date_str}'

    #         # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    #         email_message.attach(MIMEText(html, "html"))

    #         # Attach more (documents)
    #         ##############################################################
    #         attach_file_to_email(email_message, path)
    #         ##############################################################
    #         # Convert it as a string
    #         email_string = email_message.as_string()

    #         # Connect to the Gmail SMTP server and Send Email
    #         context = ssl.create_default_context()
    #         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #             server.login(email_from, password)
    #             server.sendmail(email_from, email_to, email_string)
    #         error="NO"
    #     else:
    #         error="YES"

    #     if request.method=='POST' and 'verify_otp' in request.POST:
    #         otp=request.POST['otp']
    #         if(otp==x):
    #             login(request,user)
    #             error="success"

    return render(request,"EmpLogin.html")

def validateuser(request):
    error=""
    
    empID=request.POST['EmpID']
    pwd=request.POST['pwd']
    user=authenticate(username=empID,password=pwd)
    
    if user:
        global eid
        eid=user.username
        x=random.randint(10000000,99999999)
        global otp
        otp=x
        im=qrcode.make("OTP is "+str(x))
        t=str(user.get_username())
        im.save(r"employee/static/qr/"+t+".jpg")
        path="employee/static/qr/"+t+".jpg"
        html = '''
            <html>
                <body>
                    <h1>Scan the QR code</h1>
                    <p>Enter the 8-digit OTP generated!</p>
                </body>
            </html>
            '''
        def attach_file_to_email(email_message, filename):
            with open(filename, "rb") as f:
                file_attachment = MIMEApplication(f.read())
            # Add header/name to the attachments    
            file_attachment.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            # Attach the file to the message
            email_message.attach(file_attachment)
        email_from = 'epms.major@gmail.com'
        password = 'beqcpwbqikkegvtu'
        email_to = user.email
        # Generate today's date to be included in the email Subject
        date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

        # Create a MIMEMultipart class, and set up the From, To, Subject fields
        email_message = MIMEMultipart()
        email_message['From'] = email_from
        email_message['To'] = email_to
        email_message['Subject'] = f'EPMS Validation - {date_str}'

            # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
        email_message.attach(MIMEText(html, "html"))
        attach_file_to_email(email_message, path)
        email_string = email_message.as_string()

            # Connect to the Gmail SMTP server and Send Email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_from, password)
            server.sendmail(email_from, email_to, email_string)
        error="NO"
        print(eid)
        return render(request,"qrcode_page.html")
    else:
        error="YES"

        return render(request,"EmpLogin.html",{"message":"Invalid Credentials"})
    return None

def validateOTP(request):
    user_otp=request.POST.get("otp")
    if user_otp == str(otp):
        user=User.objects.get(username=eid)
        login(request,user)
        return render(request,"EmpHome.html")
    else:
        return render(request,"EmpLogin.html",{"message":"Invalid OTP"})
    return None

def EmpHome(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    return render(request,"EmpHome.html")

def EmpPay(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    user=request.user
    employee=EmpDetail.objects.get(user=user)
    grade_detail=Grade.objects.get(position=(employee.designation))
    payroll=EmpPayroll.objects.get(user=user)

    payroll.basic=(grade_detail.basic)
    payroll.DA=(grade_detail.basic*grade_detail.DA/100)
    payroll.HRA=(grade_detail.basic*grade_detail.HRA/100)
    payroll.medical=(grade_detail.medical)
    payroll.transport=(grade_detail.transport)
    payroll.reimbursement=(grade_detail.reimbursement)
    payroll.pf=(grade_detail.basic*grade_detail.pf/100)
    payroll.esi=(grade_detail.basic*grade_detail.esi/100)
    payroll.pt=(grade_detail.basic*grade_detail.pt/100)
    payroll.tds=(grade_detail.basic*grade_detail.tds/100)
    payroll.lwf=(grade_detail.basic*grade_detail.lwf/100)
    payroll.tot_pay=(payroll.basic+payroll.DA+payroll.HRA+payroll.medical+payroll.transport+payroll.reimbursement)
    payroll.tot_ded=(payroll.pf+payroll.esi+payroll.pt+payroll.tds+payroll.lwf)
    payroll.net_pay=(payroll.tot_pay-payroll.tot_ded)
    
    try:
        payroll.save()
        error="NO"
    except:
        error="YES"
    return render(request,"EmpPay.html",locals())


def EmpProfile(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    error=""
    user=request.user
    employee=EmpDetail.objects.get(user=user)
    # grade=Grade.objects.all()
    if request.method=="POST":
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        department=request.POST['department']
        designation=request.POST['designation']
        contact=request.POST['contact']
        empID=request.POST['EmpID']
        joiningDate=request.POST['joiningDate']
        gender=request.POST['gender']
        dob=request.POST['dob']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']

        employee.user.first_name=firstname
        employee.user.last_name=lastname
        employee.middlename=middlename
        employee.department=department
        employee.designation=designation
        employee.contact=contact
        employee.empID=empID
        employee.gender=gender
        employee.address=address
        employee.city=city
        employee.state=state
        employee.zip=zip
        if joiningDate:
            employee.joiningDate=joiningDate
        if dob:
            employee.dob=dob
        
        try:
            employee.save()
            employee.user.save()
            error="NO"
        except:
            error="YES"

    return render(request,"EmpProfile.html",locals())



def Logout(request):
    logout(request)
    return redirect('index')


def EmpExp(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    user=request.user
    experience=EmpExperience.objects.get(user=user)
    return render(request,"EmpExp.html",locals())


def EditExp(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    error=""
    user=request.user
    experience=EmpExperience.objects.get(user=user)
    if request.method=="POST":
        company1Name=request.POST['company1Name']
        company1Desig=request.POST['company1Desig']
        company1Salary=request.POST['company1Salary']
        company1Duration=request.POST['company1Duration']
        
        company2Name=request.POST['company2Name']
        company2Desig=request.POST['company2Desig']
        company2Salary=request.POST['company2Salary']
        company2Duration=request.POST['company2Duration']

        company3Name=request.POST['company3Name']
        company3Desig=request.POST['company3Desig']
        company3Salary=request.POST['company3Salary']
        company3Duration=request.POST['company3Duration']
        

        experience.company1Name=company1Name
        experience.company1Desig=company1Desig
        experience.company1Salary=company1Salary
        experience.company1Duration=company1Duration

        experience.company2Name=company2Name
        experience.company2Desig=company2Desig
        experience.company2Salary=company2Salary
        experience.company2Duration=company2Duration

        experience.company3Name=company3Name
        experience.company3Desig=company3Desig
        experience.company3Salary=company3Salary
        experience.company3Duration=company3Duration
        
        try:
            experience.save()
            error="NO"
        except:
            error="YES"

    return render(request,"EditExp.html",locals())


def EmpEdu(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    user=request.user
    education=EmpEducation.objects.get(user=user)
    return render(request,"EmpEdu.html",locals())


def EditEdu(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    error=""
    user=request.user
    education=EmpEducation.objects.get(user=user)
    if request.method=="POST":
        pgCourse=request.POST['pgCourse']
        pgClg=request.POST['pgClg']
        pgYOP=request.POST['pgYOP']
        pgPercentage=request.POST['pgPercentage']
        
        gradCourse=request.POST['gradCourse']
        gradClg=request.POST['gradClg']
        gradYOP=request.POST['gradYOP']
        gradPercentage=request.POST['gradPercentage']
        
        sscSchool=request.POST['sscSchool']
        sscYOP=request.POST['sscYOP']
        sscPercentage=request.POST['sscPercentage']

        hscSchool=request.POST['sscSchool']
        hscYOP=request.POST['hscYOP']
        hscPercentage=request.POST['hscPercentage']
        
        

        education.pgCourse=pgCourse
        education.pgClg=pgClg
        education.pgYOP=pgYOP
        education.pgPercentage=pgPercentage

        education.gradCourse=gradCourse
        education.gradClg=gradClg
        education.gradYOP=gradYOP
        education.gradPercentage=gradPercentage

        education.sscSchool=sscSchool
        education.sscYOP=sscYOP
        education.sscPercentage=sscPercentage

        education.hscSchool=hscSchool
        education.hscYOP=hscYOP
        education.hscPercentage=hscPercentage
        
        
        try:
            education.save()
            error="NO"
        except:
            error="YES"

    return render(request,"EditEdu.html",locals())

def ChangePass(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    error=""
    user=request.user
    if request.method=="POST":
        currPass=request.POST['currentpassword']
        newPass=request.POST['newpassword'] 

        try:
            if user.check_password(currPass):
                flag = 0
                while True:   
                    if (len(newPass)<8): 
                        flag = -1
                        break
                    elif not re.search("[a-z]", newPass): 
                        flag = -1
                        break
                    elif not re.search("[A-Z]", newPass): 
                        flag = -1
                        break
                    elif not re.search("[0-9]", newPass): 
                        flag = -1
                        break
                    elif not re.search("[_@$]", newPass): 
                        flag = -1
                        break
                    elif re.search("\s", newPass): 
                        flag = -1
                        break
                    else: 
                        flag = 0 
                        break
                if flag==0:
                    user.set_password(newPass)
                    user.save()
                    error="NO"
                elif flag==-1:
                    error="Invalid Pass"
            else:
                error="WRONG CURRENT PASS"
        except:
            error="YES"

    return render(request,"ChangePass.html",locals())

def AdminLogin(request):
    error=""
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        user=authenticate(username=username,password=pwd)
        try:
            if user.is_staff:
                login(request,user)
                error="NO"
            else:
                error="YES"
        except:
            error="YES"
    return render(request,"AdminLogin.html",locals())


def AdminHome(request):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    return render(request,"AdminHome.html")


def AdminChangePass(request):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    error=""
    user=request.user
    if request.method=="POST":
        currPass=request.POST['currentpassword']
        newPass=request.POST['newpassword'] 

        try:
            if user.check_password(currPass):
                flag = 0
                while True:   
                    if (len(newPass)<8): 
                        flag = -1
                        break
                    elif not re.search("[a-z]", newPass): 
                        flag = -1
                        break
                    elif not re.search("[A-Z]", newPass): 
                        flag = -1
                        break
                    elif not re.search("[0-9]", newPass): 
                        flag = -1
                        break
                    elif not re.search("[_@$]", newPass): 
                        flag = -1
                        break
                    elif re.search("\s", newPass): 
                        flag = -1
                        break
                    else: 
                        flag = 0 
                        break
                if flag==0:
                    user.set_password(newPass)
                    user.save()
                    error="NO"
                elif flag==-1:
                    error="Invalid Pass"
            else:
                error="WRONG CURRENT PASS"
        except:
            error="YES"

    return render(request,"AdminChangePass.html",locals())

def AllEmployee(request):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    employee=EmpDetail.objects.all()
    return render(request,"AllEmployee.html",locals())

def DeleteEmployee(request,pid):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect("AllEmployee")


def EditProfile(request,pid,pid2):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    error=""
    employee=EmpDetail.objects.get(id=pid)
    user=User.objects.get(id=pid2)
    experience=EmpExperience.objects.get(user=user)
    education=EmpEducation.objects.get(user=user)
    grade=Grade.objects.all()
    if request.method=="POST":
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        department=request.POST['department']
        designation=request.POST['designation']
        contact=request.POST['contact']
        empID=request.POST['EmpID']
        joiningDate=request.POST['joiningDate']
        gender=request.POST['gender']
        dob=request.POST['dob']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']

        pgCourse=request.POST['pgCourse']
        pgClg=request.POST['pgClg']
        pgYOP=request.POST['pgYOP']
        pgPercentage=request.POST['pgPercentage']
        
        gradCourse=request.POST['gradCourse']
        gradClg=request.POST['gradClg']
        gradYOP=request.POST['gradYOP']
        gradPercentage=request.POST['gradPercentage']
        
        sscSchool=request.POST['sscSchool']
        sscYOP=request.POST['sscYOP']
        sscPercentage=request.POST['sscPercentage']

        hscSchool=request.POST['sscSchool']
        hscYOP=request.POST['hscYOP']
        hscPercentage=request.POST['hscPercentage']

        company1Name=request.POST['company1Name']
        company1Desig=request.POST['company1Desig']
        company1Salary=request.POST['company1Salary']
        company1Duration=request.POST['company1Duration']
        
        company2Name=request.POST['company2Name']
        company2Desig=request.POST['company2Desig']
        company2Salary=request.POST['company2Salary']
        company2Duration=request.POST['company2Duration']

        company3Name=request.POST['company3Name']
        company3Desig=request.POST['company3Desig']
        company3Salary=request.POST['company3Salary']
        company3Duration=request.POST['company3Duration']
        
        employee.user.first_name=firstname
        employee.user.last_name=lastname
        employee.middlename=middlename
        employee.department=department
        employee.designation=designation
        employee.contact=contact
        employee.empID=empID
        employee.gender=gender
        employee.address=address
        employee.city=city
        employee.state=state
        employee.zip=zip
        if joiningDate:
            employee.joiningDate=joiningDate
        if dob:
            employee.dob=dob

        education.pgCourse=pgCourse
        education.pgClg=pgClg
        education.pgYOP=pgYOP
        education.pgPercentage=pgPercentage

        education.gradCourse=gradCourse
        education.gradClg=gradClg
        education.gradYOP=gradYOP
        education.gradPercentage=gradPercentage

        education.sscSchool=sscSchool
        education.sscYOP=sscYOP
        education.sscPercentage=sscPercentage

        education.hscSchool=hscSchool
        education.hscYOP=hscYOP
        education.hscPercentage=hscPercentage

        experience.company1Name=company1Name
        experience.company1Desig=company1Desig
        experience.company1Salary=company1Salary
        experience.company1Duration=company1Duration

        experience.company2Name=company2Name
        experience.company2Desig=company2Desig
        experience.company2Salary=company2Salary
        experience.company2Duration=company2Duration

        experience.company3Name=company3Name
        experience.company3Desig=company3Desig
        experience.company3Salary=company3Salary
        experience.company3Duration=company3Duration

        try:
            employee.save()
            employee.user.save()
            education.save()
            experience.save()
            error="NO"
        except:
            error="YES"

    return render(request,"EditProfile.html",locals())

def AllPayroll(request):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    payroll=Grade.objects.all()
    return render(request,"AllPayroll.html",locals())

def DeletePayroll(request,pid):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    payroll=Grade.objects.get(id=pid)
    payroll.delete()
    return redirect("AllPayroll")

def EditPayroll(request,pid):
    if not request.user.is_authenticated:
        return redirect('AdminLogin')
    error=""
    payroll=Grade.objects.get(id=pid)
    if request.method=="POST":
        position=request.POST['position']
        basic=request.POST['basic']
        DA=request.POST['DA']
        HRA=request.POST['HRA']
        medical=request.POST['medical']
        transport=request.POST['transport']
        reimbursement=request.POST['reimbursement']
        pf=request.POST['pf']
        esi=request.POST['esi']
        pt=request.POST['pt']
        tds=request.POST['tds']
        lwf=request.POST['lwf']
        
        
        payroll.position=position
        payroll.basic=basic
        payroll.DA=DA
        payroll.HRA=HRA
        payroll.medical=medical
        payroll.transport=transport
        payroll.reimbursement=reimbursement
        payroll.pf=pf
        payroll.esi=esi
        payroll.pt=pt
        payroll.tds=tds
        payroll.lwf=lwf

        try:  
            payroll.save()
            error="NO"
        except:
            error="YES"

    return render(request,"EditPayroll.html",locals())


def AddPayroll(request):
    error=""
    if request.method=="POST":
        position=request.POST['position']
        basic=request.POST['basic']
        DA=request.POST['DA']
        HRA=request.POST['HRA']
        medical=request.POST['medical']
        transport=request.POST['transport']
        reimbursement=request.POST['reimbursement']
        pf=request.POST['pf']
        esi=request.POST['esi']
        pt=request.POST['pt']
        tds=request.POST['tds']
        lwf=request.POST['lwf']

        try:
            Grade.objects.create(position=position,basic=basic,DA=DA,HRA=HRA,medical=medical,transport=transport,reimbursement=reimbursement,pf=pf,esi=esi,pt=pt,tds=tds,lwf=lwf)
            error="NO"
        except:
            error="YES"

    return render(request,"AddPayroll.html",locals())


def AddEmployee(request):
    error=""
    if request.method=="POST":
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        email=request.POST['email']
        empID=request.POST['EmpID']
        
        
        
        try:
            user= User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=empID)
            EmpDetail.objects.create(user=user,middlename=middlename,empID=empID)
            EmpExperience.objects.create(user=user)
            EmpEducation.objects.create(user=user)
            EmpPayroll.objects.create(user=user)
            error="NO"
        except:
            error="YES"

    return render(request,"AddEmployee.html",locals())


# def render_pdf_view(request):
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def GeneratePayroll(request):
    if not request.user.is_authenticated:
        return redirect('EmpLogin')
    error=""
    user=request.user
    payroll=EmpPayroll.objects.get(user=user)
    employee=EmpDetail.objects.get(user=user)
    template_path = 'GeneratePayroll.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="payroll.pdf"'
    template = get_template(template_path)
    html = template.render(locals())
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response