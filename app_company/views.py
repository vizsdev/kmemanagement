from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import admin

from .forms import CompanyForm
from .models import Company
from .models import Role
from .forms import RoleForm
from .models import TDesignation
from .forms import DesignationForm
from .forms import EditDesignationForm
from .models import Employee
from .forms import EmployeeForm
from .models import Attendance
from .forms import AttendanceForm
from .forms import InvoiceForm
from .models import Invoice
from .forms import LogoutAttendanceForm 
from .forms import InvoiceDeliveryDueForm
from .forms import InvoiceMRAForm
from .forms import InvoicePACForm
from .forms import InvoiceFinanceForm

# from django.contrib.auth import User


# Create your views here.



def index(request):
     if request.user.is_authenticated:
          return render(request, 'home/index.html')
     else:
          return redirect('login_user')


#Login authentication
def login_user(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
                    login(request, user)
                    return redirect('index_company')
                    # Redirect to a success page.
          else:
                  messages.success(request,'Incorrect Username / Password. Please try again')
                  return redirect('login_user')
               # Return an 'invalid login' error message.
     else:
          return render(request, 'authenticate/login.html' , {})

def logout_user(request):
     logout(request)
     messages.success(request,'Successfully logged out')
     return redirect('login_user')

# def index(request):
#      return render(request, 'company/index.html',
#      {
#           'companies': Company.objects.all()
#      })

#end of view/index

#Company


def index_company(request):
     if request.user.is_authenticated:
          return render(request, 'company/index.html',
          {
               'companies': Company.objects.all()
          })   
     else:
          return redirect('login_user')


def view_company(request, companyid):
     if request.user.is_authenticated:
          company = Company.objects.get(pk=companyid) #referencing primary key from the table id
          return HttpResponseRedirect(reverse('index_company'))
     else:
          return redirect('login_user')
    
def add_Company(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               form = CompanyForm(request.POST)
               if form.is_valid():
                    form.save()
                    return render(request,'company/add.html',
                    {
                         'form': CompanyForm(),
                         'success' : True
                    })
          else:
               form = CompanyForm()
               return render(request,'company/add.html',
               {
                    'form': CompanyForm()
               })
     else:
          return redirect('login_user')

def edit_Company(request, companyid):
     if request.user.is_authenticated:     
          if request.method == 'POST':
               company= Company.objects.get(pk=companyid)
               form = CompanyForm(request.POST, instance=company)
               if form.is_valid():
                    form.save()
                    return render(request, 'company/edit.html',{
                         'form': form,
                         'success': True
                    })
          else:
               company = Company.objects.get(pk=companyid)
               form = CompanyForm(instance=company)
               return render(request, 'company/edit.html',{
                    'form': form
               })
     else:
          return redirect('login_user')

def delete_Company(request, companyid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               company = Company.objects.get(pk=companyid)
               company.delete()
               messages.add_message(request, messages.SUCCESS, 'Company deleted successfully.')
               return HttpResponseRedirect(reverse('index_company'))
     else:
          return redirect('login_user')
#End of company

#Role
def index_role(request):
     if request.user.is_authenticated:     
          return render(request, 'roles/index.html',
          {
               'roles': Role.objects.all()
          })
     else:
          return redirect('login_user')


def view_role(request, roleid):
     if request.user.is_authenticated:     
          role = Role.objects.get(pk=roleid)
          return HttpResponseRedirect(reverse('index_role'))
     else:
          return redirect('login_user')

def edit_Role(request, roleid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               role= Role.objects.get(pk=roleid)
               form = RoleForm(request.POST, instance=role)
               if form.is_valid():
                    form.save()
                    return render(request, 'roles/edit.html',{
                         'form': form,
                         'success': True
                    })
          else:
               role = Role.objects.get(pk=roleid)
               form = RoleForm(instance=role)
               return render(request, 'roles/edit.html',{
                    'form': form
               })
     else:
          return redirect('login_user')

def delete_Role(request, roleid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               role = Role.objects.get(pk=roleid)
               role.delete()
               messages.add_message(request, messages.SUCCESS, 'Role deleted successfully.')
               return HttpResponseRedirect(reverse('index_role'))
     else:
          return redirect('login_user')


def add_Role(request):
     if request.user.is_authenticated:     
          if request.method == 'POST':
               form = RoleForm(request.POST)

               if form.is_valid():
                    new_role_name = form.cleaned_data['role_name']

               
                    new_role_name=Role(
                         role_name = new_role_name
                    )

                    new_role_name.save()
                    return render(request,'roles/add.html',
                         {
                              'form': RoleForm(),
                              'success' : True
                         })
               else:
                    form = RoleForm()
                    messages.add_message(request, messages.SUCCESS, 'Role already Exists!')
                    return redirect('add_role')    
                         
          else:
               form = RoleForm()
               return render(request,'roles/add.html',
               {
                    'form': RoleForm()
               })

     else:
          return redirect('login_user')             
#End of role

#Employee

def index_employee(request):
     if request.user.is_authenticated:     
          return render(request, 'employee/index.html',
          {
               'employees': Employee.objects.all()
          })
     else:
          return redirect('login_user')


def view_employee(request, employeeid):
     if request.user.is_authenticated:     
          employee = Employee.objects.get(pk=employeeid)
          return HttpResponseRedirect(reverse('index_employee'))
     else:
          return redirect('login_user')


def edit_Employee(request, employeeid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               employee= Employee.objects.get(pk=employeeid)
               form = EmployeeForm(request.POST, instance=employee)
               if form.is_valid():
                    form.save()
                    return render(request, 'employee/edit.html',{
                         'form': form,
                         'success': True
                    })
          else:
               employee = Employee.objects.get(pk=employeeid)
               form = EmployeeForm(instance=employee)
               return render(request, 'employee/edit.html',{
                    'form': form
               })
     else:
          return redirect('login_user')


def delete_Employee(request, employeeid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               employee = Employee.objects.get(pk=employeeid)
               employee.delete()
               messages.add_message(request, messages.SUCCESS, 'Employee removed successfully.')
               return HttpResponseRedirect(reverse('index_employee'))
     else:
          return redirect('login_user')



def add_Employee(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               form = EmployeeForm(request.POST,request.FILES)

               if form.is_valid():
                         # new_employee_name = form.cleaned_data['employee_name']
                         # new_employee_birth = form.cleaned_data['employee_birth']
                         # new_employee_nationality = form.cleaned_data['employee_nationality']
                         # new_employee_passport = form.cleaned_data['employee_passport']
                         # new_employee_passport_exp = form.cleaned_data['employee_passport_exp']
                         # new_employee_eid = form.cleaned_data['employee_eid']
                         # new_employee_eid_exp = form.cleaned_data['employee_eid_exp']
                         # new_employee_visa = form.cleaned_data['employee_visa']
                         # new_employee_visa_exp = form.cleaned_data['employee_visa_exp']
                         # new_employee_photo = form.cleaned_data['employee_photo']
                         
                         # new_employee = Employee (
                         #      employee_name = new_employee_name,
                         #      employee_birth = new_employee_birth,
                         #      employee_nationality = new_employee_nationality,
                         #      employee_passport = new_employee_passport,
                         #      employee_passport_exp = new_employee_passport_exp ,
                         #      employee_eid = new_employee_eid,
                         #      employee_eid_exp = new_employee_eid_exp ,
                         #      employee_visa = new_employee_visa ,
                         #      employee_visa_exp = new_employee_visa_exp,
                         #      new_employee_photo = new_employee_photo
                              
                         # )

                         # new_employee.save()
                         form.save()
                         img_object = form.instance
                         return render(request,'employee/add.html',
                                   {
                                        'form': EmployeeForm(),
                                        'success' : True,
                                        'img_object': img_object
                                   })
               else:
                    form = EmployeeForm()
                    messages.add_message(request, messages.SUCCESS, 'This user is already assigned!')
                    return redirect('add_Employee')    
                         
          else:
               form = EmployeeForm()
               return render(request,'employee/add.html',
               {
                    'form': EmployeeForm()
               })
     else:
          return redirect('login_user')


def index_designation(request):
     if request.user.is_authenticated:
          return render(request, 'designation/index.html',
          {
               'designations': TDesignation.objects.all()
          })
     else:
          return redirect('login_user')

def view_designation(request, designationid):
     if request.user.is_authenticated:
          designation = TDesignation.objects.get(pk=designationid)
          return HttpResponseRedirect(reverse('index_designation'))
     else:
          return redirect('login_user')

def add_Designation(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               #   demployee = Employee.objects.get(pk=request.POST.get('employee_name'))
               form = DesignationForm(request.POST)

               if form.is_valid():
                    new_designation_employee = form.cleaned_data['designation_employee']
                    new_designation_role = form.cleaned_data['designation_role']
                    new_designation_start= form.cleaned_data['designation_start']
                    new_designation_end = form.cleaned_data['designation_end']

                    new_designation = TDesignation (
                         designation_employee = new_designation_employee,
                         designation_role = new_designation_role,
                         designation_start =  new_designation_start,
                         designation_end = new_designation_end
                    )

                    new_designation.save()
                    return render(request,'designation/add.html',
                         {
                              'form': DesignationForm(),
                              'success' : True
                         })
               else:
                    form = DesignationForm()
                    messages.add_message(request, messages.SUCCESS, 'This user is already assigned!')
                    return redirect('add_Designation')    
                         
          else:
               form = DesignationForm()
               return render(request,'designation/add.html',
               {
                    'form': DesignationForm()
               })
     else:
          return redirect('login_user')

def edit_Designation(request, designationid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               designation= TDesignation.objects.get(pk=designationid)
               form = EditDesignationForm(request.POST, instance=designation)
               if form.is_valid():
                    form.save()
                    return render(request, 'designation/edit.html',{
                         'form': form,
                         'success': True
                    })
          else:
               designation = TDesignation.objects.get(pk=designationid)
               form = EditDesignationForm(instance=designation)
               return render(request, 'designation/edit.html',{
                    'form': form
               })
     else:
          return redirect('login_user')


def delete_Designation(request, designationid):
     if request.user.is_authenticated:     
          if request.method == 'POST':
               designation = TDesignation.objects.get(pk=designationid)
               designation.delete()
               messages.add_message(request, messages.SUCCESS, 'Designation removed successfully.')
               return HttpResponseRedirect(reverse('index_designation'))
     else:
          return redirect('login_user')



def index_attendance(request):
     if request.user.is_authenticated:
          return render(request, 'attendance/index.html',
          {
               'attendances': Attendance.objects.all()
          })
     else:
          return redirect('login_user')


def view_attendance(request, attendanceid):
     if request.user.is_authenticated:
          attendance = Attendance.objects.get(pk=attendanceid)
          return HttpResponseRedirect(reverse('index_attendance'))
     else:
          return redirect('login_user')

def add_Attendance(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               #   demployee = Employee.objects.get(pk=request.POST.get('employee_name'))
               form = AttendanceForm(request.POST)

               if form.is_valid():
                    new_attendance_employee = form.cleaned_data['attendance_employee']
                    new_attendance_in = 'DONE'
          
                    ################################################
               
                    new_attendance = Attendance (
                         attendance_employee= new_attendance_employee,
                         attendance_in = new_attendance_in,
                    )

                    new_attendance.save()
                    return render(request,'attendance/add.html',
                         {
                              'form': AttendanceForm(),
                              'success' : True
                         })
               else:
                    form = AttendanceForm()
                    messages.add_message(request, messages.SUCCESS, 'Already submitted today!')
                    return redirect('add_Attendance')    
                         
          else:
               form = AttendanceForm()
               return render(request,'attendance/add.html',
               {
                    'form': AttendanceForm()
               })
     else:
          return redirect('login_user')




def edit_Attendance(request, attendanceid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               attendance= Attendance.objects.get(pk=attendanceid)
               form = LogoutAttendanceForm(request.POST, instance=attendance)
               if form.is_valid():
                    form.save()
                    return render(request, 'attendance/edit.html',{
                         'form': form,
                         'success': True
                    })
          else:
               attendance = Attendance.objects.get(pk=attendanceid)
               form = LogoutAttendanceForm(instance=attendance)
               return render(request, 'attendance/edit.html',{
                    'form': form
     
               })

     else:
          return redirect('login_user')


 #Start of Invoice
 
def index_invoice(request):
     if request.user.is_authenticated:
          return render(request, 'invoice/index.html',
                         {
                              'invoice': Invoice.objects.all()
                         })
     else:
          return redirect('login_user')

@admin.register(Invoice)
class ExampleAdmin(admin.ModelAdmin):
        list_display = ('price_formatted',)

# def view_invoice(request, invoiceid):
#      if request.method == 'POST':
#           invoice = Invoice.objects.get(pk=invoiceid)
#           form = InvoiceForm(request.POST,request.FILES, instance=invoice)
#           if form.is_valid():
#                form.save()
#                doc_object = form.instance
#                return render(request, 'invoice/view.html', {
#                     'form': form,
#                     'success': True,
#                     'doc_object': doc_object
#                })
#      else:
#                invoice = Invoice.objects.get(pk=invoiceid)
#                form = InvoiceForm(instance=invoice)
#                return render(request, 'invoice/view.html', {
#                     'form': form
#                })

def view_invoice(request, invoiceid):
     if request.user.is_authenticated:
          invoice = Invoice.objects.get(pk=invoiceid) # we insert this line to get the Band with that id
          return render(request,'invoice/view.html',{'invoice': invoice}) # we update this line to pass the band to the template
     else:
          return redirect('login_user')

def edit_invoice(request, invoiceid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceForm(request.POST,request.FILES, instance=invoice)
               if form.is_valid():
                    form.save()
                    doc_object = form.instance
                    return render(request, 'invoice/edit.html', {
                         'form': form,
                         'success': True,
                         'doc_object': doc_object
                    })
          else:
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceForm(instance=invoice)
               return render(request, 'invoice/edit.html', {
                    'form': form
               })
     else:
          return redirect('login_user')    



def delete_invoice(request, invoiceid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               invoice = Invoice.objects.get(pk=invoiceid)
               invoice.delete()
               messages.add_message(request, messages.SUCCESS, 'Invoice removed succefully.')
               return HttpResponseRedirect(reverse('index_invoice'))
     else:
          return redirect('login_user')   



def add_invoice(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               form = InvoiceForm(request.POST,request.FILES)
               if form.is_valid():
                    
                    # SAVE DATA 
                    form.save()
                    doc_object = form.instance
                    return render(request, 'invoice/add.html', {
                                   'form': InvoiceForm(),
                                   'success': True,
                                   'doc_object': doc_object
                              })
               
               else:
                    form = InvoiceForm()
                    return render(request, 'invoice/add.html' ,
                    {
                    'form': InvoiceForm()
                    })
          else:
               form = InvoiceForm()
               return render(request, 'invoice/add.html' ,
               {
               'form': InvoiceForm()
               })
     else:
          return redirect('login_user')


def edit_dsu(request, invoiceid): 
     if request.user.is_authenticated:
          if request.method == 'POST':
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceDeliveryDueForm(request.POST, instance=invoice)
               if form.is_valid():
                    form.save()
                    return render(request, 'invoice/dsu.html', {
                         'form': form,
                         'success': True
                    })
          else:
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceDeliveryDueForm(instance=invoice)
               return render(request, 'invoice/dsu.html', {
                    'form': form
               })
     else:
          return redirect('login_user')     

def edit_mrau(request, invoiceid):
     if request.user.is_authenticated:     
          if request.method == 'POST':
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceMRAForm(request.POST, instance=invoice)
               if form.is_valid():
                    form.save()
               
                    return render(request, 'invoice/mrau.html', {
                         'form': form,
                         'success': True
                    })
          else:
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceMRAForm(instance=invoice)
               return render(request, 'invoice/edit.html', {
                              'form': form
          })
     else:
          return redirect('login_user')



def edit_pacu(request, invoiceid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoicePACForm(request.POST, instance=invoice)
               if form.is_valid():
                    form.save()
                    return render(request, 'invoice/pacu.html', {
                         'form': form,
                         'success': True
                    
                    })
          else:
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoicePACForm(instance=invoice)
               return render(request, 'invoice/pacu.html', {
                         'form': form
               })
     else:
          return redirect('login_user')


def edit_finu(request, invoiceid):
     if request.user.is_authenticated:
          if request.method == 'POST':
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceFinanceForm(request.POST, instance=invoice)
               if form.is_valid():
                    form.save()
                    doc_object = form.instance
                    return render(request, 'invoice/finu.html', {
                         'form': form,
                         'success': True
                    })
          else:
               invoice = Invoice.objects.get(pk=invoiceid)
               form = InvoiceFinanceForm(instance=invoice)
               return render(request, 'invoice/finu.html', {
                         'form': form
               })
     else:
          return redirect('login_user')

 #End of Invoice

# Entry.objects.values_list('headline', flat=True).get(pk=1)
#  # End of Designation


# Imaginary function to handle an uploaded file.

# FILE UPLOAD USING VIEW
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})




# #FILE UPLOAD USING MODEL
# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})


# # FILE HANDLE WITH VIEWS
# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

