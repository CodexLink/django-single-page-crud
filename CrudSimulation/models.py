from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from .additionals.metaData import *

# Create your models here.
def user_src_avatar_path(instance, filename):
    return 'userdata/avatar_{0}/{1}'.format(instance.unique_id, filename)

class UserDepartment(models.Model):
    class Meta:
        verbose_name = "User Assigned Department"
        db_table = "user_department"

    Department_Name = models.CharField(max_length=32, null=False, blank=False, verbose_name="Department Name", help_text="Department Unique Identity. Make it formalized by using Title Case as possible.")
    Department_SName = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name="Department CodeName", help_text="Department Description. This describes the department's objective and goal. Actually you can write anything that you like.")
    Department_UUID = models.UUIDField(max_length=32, default=uuid4, editable=False, unique=True, help_text="A Unique Identifier for the Department. Used for references and any other such.")

    def __str__(self):
        return '%s — %s |> UUID %s' % (self.Department_Name, self.Department_SName, self.Department_UUID)

class UserRoles(models.Model):
    class Meta:
        verbose_name = "User Role"
        db_table = "user_roles"

    Role_Name = models.CharField(max_length=32, null=False, blank=False, unique=True, verbose_name="User Role Name", help_text="A group-scoped identifier used to name what they really are. Selected Role is allowed.")
    Role_Description = models.CharField(max_length=64, null=False, blank=False, verbose_name="User Role Description", help_text="A identifier description. Write anything that you like here based from what you interpret to this particular role.")

    def __str__(self):
        return '%s | %s ' % (self.Role_Name, self.Role_Description)

class UserCredentials(AbstractUser):
    class Meta:
        verbose_name= "User Admin Meta Data"
        db_table= "user_admin_credentials"
        permissions = [
            ("limited_access", "A user who have this permission have limited capabilities such as the inabilty to edit the data."),
            ("data_viewable", "A user who have this permission can view the web-app that contains personal information."),
            ("user_require", "A user should must be able to have this permission to access the website itself.")
        ]

    middle_name = models.CharField(max_length=20, null=True, blank=True, help_text="A Name that is not supplied by User Model. Added for Unique User Purposes.")
    uuid = models.UUIDField(max_length=32, default=uuid4, editable=False, unique=True, help_text="A Unique Identifier for your Account. This is used for DB authentication and references. Please DO NOT SHARE IT OUTSIDE.")
    role = models.ForeignKey(UserRoles, to_field="Role_Name", null=True, blank=True, verbose_name="User Role", help_text="A Group-Scoped Identifier for who should be dominating at your group.", on_delete=models.CASCADE)
    dept_residence = models.ForeignKey(UserDepartment, to_field="Department_SName", null=True, blank=True, verbose_name="User Assigned Deparment", help_text="Assigned Deparment. Literally a department assigned to this particular person.", on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_src_avatar_path)

    def __str__(self):
        return '%s | %s %s %s | %s | %s' % (self.username, self.first_name, self.middle_name, self.last_name, self.role, self.dept_residence)

class UserTasks(models.Model):
    class Meta:
        verbose_name = "User Task"
        db_table = "user_tasks"

    Task_Name = models.CharField(max_length=32, null=False, blank=False, verbose_name="Task Name", help_text="Unique Identifier for Task Assigned To Users.")
    Task_Description = models.CharField(max_length=256, null=False, blank=False, verbose_name="Task Description", help_text="Literally Task Description. Required. You have to point out what's the point of the task given to you.")
    Task_Type = models.CharField(max_length=16, null=False, blank=False, verbose_name="Task Type", choices=TaskTypes, default=TaskTypes[0][0], help_text="Literally A Task Type. This could help users how important the task is.")
    Task_StartTime = models.DateTimeField(verbose_name='Task Start Time', help_text='Refers to a time start of the task.', null=True, blank=True)
    Task_EndTime = models.DateTimeField(verbose_name='Task End Time', help_text='Refers to a time end of the task.', null=True, blank=True)
    Task_CreateDate = models.DateTimeField(auto_now_add=True, verbose_name='Task Creation Date & Time', help_text="Refers to a time from where the task has been created.", null=False, blank=False, editable=False)

    def __str__(self):
        return '%s | %s | %s |> Created as of ' % (self.Task_Name, self.Task_Description, self.Task_Type, self.Task_CreateDate)