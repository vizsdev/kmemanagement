from django.db import models
from django import forms
from django.contrib import admin
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import uuid 
import pytz
utc=pytz.UTC


from django_countries.fields import CountryField
from django.db.models import CheckConstraint, Q, F
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

#User 

# Company Model
class Company(models.Model):
    company_id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,serialize=False)
    company_name = models.TextField(max_length=50)
    company_address = models.CharField(max_length=100)
    company_location=CountryField()
    company_est = models.DateTimeField(max_length=10)
    company_created_at = models.DateTimeField(auto_now_add=True)
    company_updated_at = models.DateTimeField(auto_now=True)
    company_updated_by = models.CharField(auto_created=True, max_length=50)
    
    def __str__(self) -> str:
        return self.company_name # END of Company Model


#Role MODEL

class Role(models.Model):
    role_id=models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False,serialize=False)
    role_name=models.CharField(max_length=20,unique=True)
    role_created_at = models.DateTimeField(auto_now_add=True)
    role_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        # return f'Role:{self.role_name}'
         return self.role_name
    # class Meta:
    #         ordering = ['-role_name']
    #         constraints = [
    #             models.UniqueConstraint(fields=['role_name'], name='Role already exists')
    #         ]
# End of role model

class Employee(models.Model):
    Gender = [
        ('','Select Gender'),
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    ]
    # employee_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True, editable=False)
    employee_id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,serialize=False)
    employee_firstname=models.CharField(max_length=50)
    employee_middlename=models.CharField(max_length=50)
    employee_lastname=models.CharField(max_length=50)
    employee_birth=models.CharField(max_length=20)
    employee_gender = models.CharField(max_length=10, choices=Gender,default="")
    employee_nationality=CountryField()
    employee_passport=models.CharField(max_length=30, unique=True) #to be encrypted
    employee_passport_exp=models.DateTimeField(max_length=20)
    employee_eid=models.CharField(max_length=30, unique=True) #to be encrypted
    employee_eid_exp=models.DateTimeField()
    employee_visa=models.CharField(max_length=30, unique=True) #to be encrpyted
    employee_visa_exp=models.DateTimeField(max_length=20)
    employee_created_at = models.DateTimeField(auto_now_add=True)
    employee_updated_at = models.DateTimeField(auto_now=True)
    employee_photo = models.FileField(upload_to='images')

    def __str__(self) -> str:
       return f'{self.employee_firstname} {self.employee_middlename} {self.employee_lastname}'
        # return self.employee_nationality
   
    def dehydrate_country(self, bundle):
        return bundle.obj.country.name 

    @property
    def employee_fullname(self):
        return self.employee_firstname+ ' ' + self.employee_middlename + ' ' + self.employee_lastname 
    # @property
    # def is_in_category(self):
    #     # 'calculation' return a boolean
    #     return True if something else False


    ##NEED TO IMPORT AND INSTALL PYZ TO USE BELOW CODE
    @property
    def eid_expired(self):
        return datetime.utcnow().replace(tzinfo=pytz.UTC) >= self.employee_eid_exp

    @property
    def eid_expiring(self):
        # new_date = parser.parse(self.employee_eid_exp)
        # if past > new_date :
        #     print("This is older than 90 days")
        return timedelta(days=90) >=  self.employee_eid_exp - datetime.utcnow().replace(tzinfo=pytz.UTC) 


# End of Employee model

class Department(models.Model):
    department_id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,serialize=False)
    department_name = models.CharField(max_length=50)
    department_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department_created_at = models.DateTimeField(auto_now_add=True)
    department_updated_at = models.DateTimeField(auto_now=True)


class TDesignation(models.Model):
    designation_id=models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,serialize=False)
    designation_start= models.CharField(max_length=20, null = True)
    designation_end = models.CharField(max_length=20, null = True)
    designation_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    designation_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
    designation_created_at = models.DateTimeField(auto_now_add=True)
    designation_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
    #  return f'TDesignation:{self.designation_id}{self.designation_employee.employee_name}{self.designation_role.role_name}{self.designation_start}{self.designation_end}'
     return self.designation_employee.employee_name


class Attendance (models.Model):
    attendance_id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,serialize=False)
    attendance_employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_in = models.CharField(max_length=20,blank=True,null=True)    
    attendance_timein = models.DateTimeField(auto_now_add=True)
    attendance_out = models.CharField(max_length=20,blank=True,null=True)
    attendance_timeout = models.DateTimeField(auto_now = True, blank=True,null=True)

    def __str__(self) -> str:
    #  return f'TDesignation:{self.designation_id}{self.designation_employee.employee_name}{self.designation_role.role_name}{self.designation_start}{self.designation_end}'
     return self.attendance_employee

#Start of Invoice model

class Invoice(models.Model):
    Status = [
        ('','Select Status'),
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    ]
    invoice_id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, serialize=False)
    invoice_customer_po = models.CharField(max_length=15)
    invoice_number = models.CharField(max_length=20)
    invoice_order_prodinfo = models.CharField(max_length=100)
    invoice_order_quantity = models.DecimalField(max_digits=10, decimal_places=0)
    #FOC
    invoice_foc_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    invoice_foc_quantity = models.DecimalField(max_digits=10, decimal_places=0)
    invoice_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_net_value = models.DecimalField(max_digits=10, decimal_places=0)
    invoice_delivery_due_date = models.DateTimeField(max_length=10)
    invoice_delivery_due_date_status = models.CharField(max_length=10, choices=Status,default="Pending",null=False,blank=False)
    invoice_issue_date = models.DateTimeField(max_length=10)
    invoice_mra_date = models.DateTimeField(max_length=10)
    invoice_mra_date_status = models.CharField(max_length=10, choices=Status,default="Pending",null=False,blank=False)
    invoice_pac_date = models.DateTimeField(max_length=10)
    invoice_pac_date_status = models.CharField(max_length=10, choices=Status,default="Pending",null=False,blank=False)
    invoice_finance_date = models.DateTimeField(max_length=10)
    invoice_finance_date_status = models.CharField(max_length=10, choices=Status,default="Pending",null=False,blank=False)
    invoice_created_at = models.DateTimeField(auto_now_add=True)
    invoice_updated_at = models.DateTimeField(auto_now=True)
    invoice_document_0 = models.FileField(upload_to='documents',blank=True,null=True)
    invoice_document_1 = models.FileField(upload_to='documents',blank=True,null=True)
    invoice_document_2 = models.FileField(upload_to='documents',blank=True,null=True)
    invoice_document_3 = models.FileField(upload_to='documents',blank=True,null=True)
    invoice_document_4 = models.FileField(upload_to='documents',blank=True,null=True)
    
    def __str__(self):
        return self.name

    @property
    @admin.display(description='invoice_order_quantity', ordering='invoice_order_quantity')
    def price_formatted(self):
        return f'{self.invoice_order_quantity:,}'

    #Define model calculation
    def save(self, *args, **kwargs):
        self.invoice_foc_quantity = self.invoice_order_quantity * self.invoice_foc_percentage/100
        self.invoice_net_value= self.invoice_order_quantity * self.invoice_unit_price
        super().save(*args, **kwargs)
 
    @property
    def get_delivery_due_progress(self):
        # (difference of current from start date / difference of final date from start date) * 100
        # (today - issuedate) / (duedate - issuedate)  *100
        # due_date= self.invoice_delivery_due_date.day()
        # today = datetime.today().replace(tzinfo=pytz.UTC)
        rem1 = datetime.utcnow().replace(tzinfo=pytz.UTC) - self.invoice_issue_date
        rem2 = self.invoice_delivery_due_date - self.invoice_issue_date
        stats = rem1/rem2 * 100
        # remm = timedelta(days=rem)
        # due_date_calc = self.invoice_issue_date - self.invoice_delivery_due_date
        # due_date = due_date.strftime ("%d")
        # today = datetime.now().strftime ("%Y%m%d")
        return str(stats)

    @property
    def get_delivery_total_days(self):
        # (duedate - issuedate) / (duedate - issuedate)  *100
        totalcalc = self.invoice_delivery_due_date - self.invoice_issue_date 
        totaldays = totalcalc / totalcalc * 100
        return totaldays
          
    # @property
    # def get_mra_days(self):
    #     # (duedate - issuedate) / (duedate - issuedate)  *100
    #     mra1 = datetime.utcnow().replace(tzinfo=pytz.UTC) - self.invoice_mra_date
    #     totaldays = totalcalc / totalcalc * 100
    #     return totaldays


    #    -  datetime.today().replace(tzinfo=pytz.UTC).day()
    

#End of Invoice model

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()






# class Reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateTimeField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.headline

#     class Meta:
#         ordering = ['headline']



###############################

#User Model

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.ManyToManyField("self",
#         related_name="assigned_to",
#         symmetrical= False,
#         blank=True
#         )


#     def __str__(self):
#         return self.user.username

