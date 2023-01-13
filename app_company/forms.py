from django import forms
from django_countries.widgets import CountrySelectWidget


from .models import Company
from .models import Role
from .models import Employee
from .models import TDesignation
from .models import Attendance
from .models import Invoice
from django.db.models import CheckConstraint, Q, F
# from .models import Designation


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=


class CompanyForm(forms.ModelForm):
      class Meta:
        model = Company
        fields = ['company_name','company_location','company_address','company_est'] #'__all__' to display all fields#
        # fields= '__all__'  (to display all fields#)
        
        # Do this if not assigned in models.py
        labels = {
          'company_name': 'Company Name',
          'company_location': 'Location',
          'company_address': 'Address',
          'company_est': 'Year Established'
        }

        widgets = {
        'company_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter desired name'}),
        'company_location' : CountrySelectWidget(attrs={'class':'form-control'}),
        'company_address':  forms.Textarea(attrs={'class':'form-control'}),
        'company_est':  forms.DateInput(attrs={'class': 'form-control','placeholder': 'Company Established','type': 'date', 'class':'form-control'}),  }
#end of company


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']

        labels ={'role_name' : "Role"}

        widgets = {'role_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter role name',})}

#end of role


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_firstname','employee_middlename','employee_lastname','employee_birth','employee_gender','employee_nationality','employee_passport','employee_passport_exp','employee_eid','employee_eid_exp','employee_visa','employee_visa_exp','employee_photo'] #'__all__' to display all fields#
        # fields= '__all__'  (to display all fields#)
    
        labels = {
        'employee_firstname': 'First Name',
        'employee_middlename': 'Middle Name',
        'employee_lastname' : 'Last Name',
        'employee_birth': 'Birthday',
        'employee_gender': 'Gender',
        'employee_nationality': 'Nationality',
        'employee_passport' : 'Passport Number',
        'employee_passport_exp': 'Passport Expiry',
        'employee_eid': 'Emirates ID',
        'employee_eid_exp': 'Emirates ID Expiry',
        'employee_visa': 'Residence Visa',
        'employee_visa_exp' : 'Visa Expiry',
        'employee_photo' : "Photo",

        }

        widgets = {
        'employee_firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter first name'}),
        'employee_middlename': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter middle name'}),
        'employee_lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter last name'}),
        'employee_birth' : forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date', 'class':'form-control'}),
        'employee_gender' : forms.Select(attrs={'class':'form-control','value':'SELECT GENDER'}),
        'employee_nationality' : CountrySelectWidget(attrs={'class':'form-control'}),
        'employee_passport' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter passport number'}),
        'employee_passport_exp' : forms.DateInput(attrs={'class': 'form-control','placeholder': 'Passport expiry date','type': 'date', 'class':'form-control'}),
        'employee_eid' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter Emirates ID number'}),
        'employee_eid_exp': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Emirates ID expiry date','type': 'date', 'class':'form-control'}),
        'employee_visa': forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Enter visa number'}),
        'employee_visa_exp' : forms.DateInput(attrs={'class': 'form-control','placeholder': 'Visa expiry date','type': 'date', 'class':'form-control'}),
        'employee_photo' : forms.FileInput()
        }

class DesignationForm(forms.ModelForm):
    class Meta:
        model= TDesignation
        fields = ['designation_employee','designation_role','designation_start','designation_end']
        labels = { 
            'designation_employee' : 'Employee Name',
            'designation_role': 'Role',
            'designation_start' : 'Designation Start',
            'designation_end' : 'Designation End' 
        }
        
        widgets = {
        'designation_employee' : forms.Select(attrs={'class':'form-control','placeholder' : 'Select Employee'}),
        'designation_role'  : forms.Select(attrs={'class':'form-control','placeholder' : 'Select Role'}),
        'designation_start' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Employment start date','type': 'date', 'class':'form-control'}),
        'designation_end' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Designation end date','type': 'date', 'class':'form-control'}),
         }

class EditDesignationForm(forms.ModelForm):
    class Meta:
        model= TDesignation
        fields = ['designation_employee','designation_role','designation_start','designation_end']
        labels = { 
            'designation_employee' : 'Employee Name',
            'designation_role': 'Role',
            'designation_start' : 'Designation Start',
            'designation_end' : 'Designation End' 
        }
        
        widgets = {
        'designation_employee' : forms.Select(attrs={"disabled":"disabled",'class':'form-control'}),
        'designation_role'  : forms.Select(attrs={'class':'form-control'}),
        'designation_start' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Employment start date','type': 'date'}),
        'designation_end' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Designation end date','type': 'date', 'class':'form-control'}),
         }
        # drole = forms.ModelChoiceField(queryset=Role.objects.values('role_name'))

# class TDesignationSerializer(serializers.ModelSerializer):
#     deisgnation_employee = serializers.StringRelatedField(many=True)
#     class Meta(object):
        
#         model = TDesignation
      
#         fields = 'designation_employee'

# form = DesignationForm()

# demployee = Employee.objects.get(pk=1)
# form = DesignationForm(instance=demployee)


class AttendanceForm(forms.ModelForm):
    class Meta:
        model= Attendance
        fields = ['attendance_employee']
        labels = { 
            'attendance_employee' : 'Employee Name',
         
        }
        
        widgets = {
        'attendance_employee': forms.Select(attrs={'class':'form-control'}),
      
        }

class LogoutAttendanceForm(forms.ModelForm):
    class Meta:
        model= Attendance
        fields = ['attendance_employee','attendance_out']
        labels = {'attendance_employee':'Employee', 'attendance_out' : ''}
        
        widgets = {
        'attendance_employee': forms.Select(attrs={'class':'form-control read' ,'tabindex' : '-1'}),
        'attendance_out': forms.TextInput(attrs={'hidden':'hidden', 'value': 'DONE'})

        }




    
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_customer_po', 'invoice_number', 'invoice_order_prodinfo' ,'invoice_order_quantity', 'invoice_foc_percentage', 'invoice_unit_price', 'invoice_issue_date', 'invoice_delivery_due_date', 'invoice_mra_date', 'invoice_pac_date', 'invoice_finance_date','invoice_document_0','invoice_document_1','invoice_document_2','invoice_document_3','invoice_document_4']

        labels = {
            'invoice_customer_po' : 'Customer PO Number', 
            'invoice_number' : 'Invoice Number', 
            'invoice_order_prodinfo' : 'Order Information',
            'invoice_order_quantity' : 'Order Quantity', 
            'invoice_foc_percentage': 'FOC %', 
            'invoice_unit_price' : 'Unit Price in USD $', 
            'invoice_issue_date' : 'Invoice Issue Date', 
            'invoice_delivery_due_date' : 'Delivery Due Date', 
            'invoice_mra_date' : 'MRA Date', 
            'invoice_pac_date' : 'PAC Date', 
            'invoice_finance_date' : 'Finance Date',
            'invoice_document_0' : 'Supporting document #1' ,
            'invoice_document_1': 'Supporting document #2 ',
            'invoice_document_2' : 'Supporting document #3 ',
            'invoice_document_3' : 'Supporting document #4 ',
            'invoice_document_4' : 'Supporting document #5 '
        }
        widgets = {
            'invoice_customer_po': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter PO Number'}),
            'invoice_number': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter invoice number'}),
            'invoice_order_prodinfo': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter product order information'}),
            'invoice_order_quantity': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter quantity'}),
            'invoice_foc_percentage': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter FOC %','min':'1','max':'200'}),
            # 'invoice_foc_quantity': forms.NumberInput(attrs={'class':'form-control', 'placeholder': ' Order Quantity x FOC%','disabled':'disabled'}),
            'invoice_unit_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter Price'}),
            # 'invoice_net_value': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Order quantity x Unit price','disabled':'disabled'}),
            'invoice_issue_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date', 'class':'form-control'}),
            'invoice_delivery_due_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date', 'class':'form-control'}),
            'invoice_mra_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date', 'class':'form-control'}),
            'invoice_pac_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date', 'class':'form-control'}),
            'invoice_finance_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date', 'class':'form-control'}),
            'invoice_document_0' : forms.FileInput(),
            'invoice_document_1': forms.FileInput(),
            'invoice_document_2' : forms.FileInput(),
            'invoice_document_3' : forms.FileInput(),
            'invoice_document_4' : forms.FileInput(),

        }


class InvoiceDeliveryDueForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [ 'invoice_delivery_due_date_status', ]

        labels = {
            'invoice_delivery_due_date_status' : 'Delivery Status'
        }
        widgets = {
            'invoice_delivery_due_date_status':  forms.Select(attrs={'class':'form-control'}),
        }   

class InvoiceMRAForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [ 'invoice_mra_date_status']

        labels = {
    
           
            'invoice_mra_date_status' : 'MRA Status', 
           
           
        }
        widgets = {
            'invoice_mra_date_status':  forms.Select(attrs={'class':'form-control'}),

        }   

class InvoicePACForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_pac_date_status']

        labels = {
            'invoice_pac_date_status' : 'PAC Status', 
           
           
        }
        widgets = {
             'invoice_pac_date_status':  forms.Select(attrs={'class':'form-control'}),

        }   

class InvoiceFinanceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_finance_date_status']

        labels = {
            'invoice_finance_date_status' : 'Finance Status', 
        }
        widgets = {
             'invoice_finance_date_status': forms.Select(attrs={'class':'form-control'}),
        }   


     
        # def __init__(self, *args, **kwargs):
        #     super(LogoutAttendanceForm, self).__init__(*args, **kwargs)
        #     self.fields['attendance_employee'].disabled = True
        #     self.fields['attendance_employee'].initial = self.instance.attendance_employee


        # def __init__(self, *args, **kwargs):

        # # If the form has been submitted, populate the disabled field
        #     if 'data' in kwargs:
        #         data = kwargs['data'].copy()
        #         self.prefix = kwargs.get('prefix')
        #         data[self.add_prefix('myfield')] = MY_VALUE
        #         kwargs['data'] = data

        #     super(MyForm, self).__init__(*args, **kwargs)     


        # def __init__(self, *args, **kwargs):
        #     super(LogoutAttendanceForm, self).__init__(*args, **kwargs)
        #     self.data.update({ 'attendance_employee': self.instance.attendance_employee })

        # If the form has been submitted, populate the disabled field

    


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()