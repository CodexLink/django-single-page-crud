from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserDepartmentAttributes(admin.ModelAdmin):
    model = UserDepartment
    list_display = ("Department_Name", "Department_SName", "Department_UUID")
    list_filter = ("Department_Name", "Department_SName", "Department_UUID")
    readonly_fields = ("Department_UUID", )

# class UserRolesAttributes(admin.ModelAdmin):
#     model = UserRoles
#     list_display = ("Role_Name", "Role_Description")
#     list_filter = ("Role_Name", "Role_Description")

class UserCredentialsAttributes(UserAdmin):
    model = UserCredentials
    list_display = ("username", "first_name", "middle_name", "last_name", "dept_residence", 'is_active' ,'is_staff', 'is_superuser', 'date_joined', "uuid")
    list_filter = ("username", "first_name", "middle_name", "last_name", "dept_residence", 'is_active' ,'is_staff', 'is_superuser', 'date_joined', "uuid")
    readonly_fields = ("uuid", )
    fieldsets =  (
        ('User Credentials', {
            'fields': ('username', 'password', 'dept_residence'),
            }
        ),
        ('User Information', {
            'fields': ('first_name', 'middle_name', 'last_name', 'avatar'),
            }
        ),
        ('Permissions and Restrictions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
            }
        ),
        ('Dates | Last Login and Creation Time', {
            'fields': ('last_login', 'date_joined'),
            }
        ),
        ('Technical Information', {
            'fields': ('uuid',),
            }
        ),
    )
    add_fieldsets = (
        ('User Credentials', {
            'fields': ('username', 'password1', 'password2', 'dept_residence'),
            }
        ),
        ('User Information', {
            'fields': ('first_name', 'middle_name', 'last_name', 'avatar'),
            }
        ),
        ('Permissions and Restrictions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
            }
        ),
        ('Technical Information', {
            'fields': ('uuid',),
            }
        ),
    )

class UserTasksAttributes(admin.ModelAdmin):
    model = UserTasks
    list_display = ("Task_Name", "Task_Description", "Task_Type", "Task_StartTime", "Task_EndTime", "Task_CreateDate", "Task_UUID")
    list_filter = ("Task_Name", "Task_Description", "Task_Type", "Task_StartTime", "Task_EndTime", "Task_CreateDate", "Task_UUID")

admin.site.register(UserDepartment, UserDepartmentAttributes)
# admin.site.register(UserRoles, UserRolesAttributes)
admin.site.register(UserCredentials, UserCredentialsAttributes)
admin.site.register(UserTasks, UserTasksAttributes)
