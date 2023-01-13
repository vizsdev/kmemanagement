from django.urls import path
from . import views

#if error 'set' object is not reversible is observed, change "{" "}" bracket to "[" "]"
urlpatterns = [
    
    path('', views.index, name='index_company'),



    #LOGIN & LOGOUT
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),

    #COMPANY
    path('company/index/', views.index_company, name='index_company'),
    path('<uuid:companyid>', views.view_company, name='view_company'), #creates dynamic URL    
    path('company/add/',views.add_Company, name='add_company'),
    path('company/edit/<uuid:companyid>/', views.edit_Company, name='edit_company'),
    path('company/delete/<uuid:companyid>/', views.delete_Company, name='delete_company'),


    #ROLE
    path('roles/index/', views.index_role, name='index_role'),
    path('<uuid:roleid>',views.view_role, name='view_role'),
    path('roles/add/',views.add_Role, name='add_role'),
    path('role/edit/<uuid:roleid>/', views.edit_Role, name='edit_role'),
    path('role/delete/<uuid:roleid>/', views.delete_Role, name='delete_role'),


    #Employee
    path('employee/index/', views.index_employee, name='index_employee'),
    path('<uuid:employeeid>',views.view_employee, name='view_employee'),
    path('employee/add/',views.add_Employee, name='add_Employee'),
    path('employee/edit/<uuid:employeeid>/', views.edit_Employee, name='edit_Employee'),
    path('employee/delete/<uuid:employeeid>/', views.delete_Employee, name='delete_Employee'),


    #Designation
    path('designation/index/', views.index_designation, name='index_designation'),
    path('<uuid:designationid>',views.view_designation, name='view_designation'),
    path('designation/add/',views.add_Designation, name='add_Designation'),
    path('designation/edit/<uuid:designationid>/', views.edit_Designation, name='edit_Designation'),
    path('designation/delete/<uuid:designationid>/', views.delete_Designation, name='delete_Designation'),



    #Attendance
    path('attendance/index/', views.index_attendance, name='index_attendance'),
    path('<uuid:attendanceid>',views.view_attendance, name='view_attendance'),
    path('attendance/add/',views.add_Attendance, name='add_Attendance'),
    path('attendance/edit/<uuid:attendanceid>/', views.edit_Attendance, name='edit_Attendance'),
    # path('attendance/delete/<int:attendanceid>/', views.delete_Attendance, name='delete_Attendance'),


    #Invoice
    path('invoice/index/', views.index_invoice, name='index_invoice'),
    path('invoice/view/<uuid:invoiceid>/',views.view_invoice, name='view_invoice'),
    path('invoice/add/',views.add_invoice, name='add_invoice'),
    path('invoice/edit/<uuid:invoiceid>/', views.edit_invoice, name='edit_invoice'),
    path('invoice/delete/<uuid:invoiceid>/', views.delete_invoice, name='delete_invoice'),
    path('invoice/dsu/<uuid:invoiceid>/', views.edit_dsu, name='edit_dsu'),
    path('invoice/mrau/<uuid:invoiceid>/', views.edit_mrau, name='edit_mrau'),
    path('invoice/pacu/<uuid:invoiceid>/', views.edit_pacu, name='edit_pacu'),
    path('invoice/finu/<uuid:invoiceid>/', views.edit_finu, name='edit_finu'),


    
]