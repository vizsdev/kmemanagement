from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Company
from .models import Role
from .models import Employee
from .models import TDesignation
from .models import Attendance


# Register your models here.
admin.site.register(Company)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(TDesignation)
admin.site.register(Attendance)


# #Unregister
# admin.site.unregister(Group)



# #Extend User Model
# class UserAdmin(admin.ModelAdmin):
  
#         model = User
#     #Just display username fields on admin page

    
#         fields = ["username","password","email"]
    
#         labels =  {
#         'username': 'Username',
#         'password': 'Password',
#         'email' : 'Email'
        
#         }

   
   

# #unregister initial user
# admin.site.unregister(User)

# #Reregister user
# admin.site.register(User, UserAdmin)
# admin.site.register(Profile)