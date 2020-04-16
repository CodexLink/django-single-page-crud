from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .additionals.metaData import *
from .models import UserCredentials, UserTasks, UserDepartment
from django.contrib.auth.forms import AuthenticationForm

class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = UserCredentials
        fields = ['username', 'password']
    username = forms.CharField(min_length=2, max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationUsername', 'placeholder': 'Required'}))
    password = forms.CharField(min_length=2, max_length=128, required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'validationPassword', 'placeholder': 'Required'}))

class UserTaskAdditionForm(forms.ModelForm):
    class Meta:
        model = UserTasks
        fields = '__all__'
        exclude = ['Task_UUID', 'Task_CreateDate', 'Task_Owner']

    Task_Name = forms.CharField(min_length=2, max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'addDataTaskName', 'placeholder': 'Required'}))
    Task_Description = forms.CharField(min_length=2, max_length=512, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id':'addTaskDescription', 'placeholder': 'Required'}))
    Task_Type = forms.ChoiceField(choices=TaskTypes, required=True, widget=forms.Select(attrs={'class': 'form-control', 'id':'addDataTaskType', 'placeholder': 'Required'}))
    Task_StartTime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'addTaskStartTime', 'placeholder': 'Start DateTime', 'type': 'datetime-local', 'min': '2020/04/01T000:00', 'max': '2099/12/31T000:00' }))
    Task_EndTime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'addTaskEndTime', 'placeholder': 'End DateTime', 'type': 'datetime-local', 'min': '2020/04/01T000:00', 'max': '2099/12/31T000:00' }))


class UserTaskUpdateForm(forms.ModelForm):
    class Meta:
        model = UserTasks
        fields = '__all__'
        exclude = ['Task_UUID', 'Task_CreateDate', 'Task_Owner']

    Task_Name = forms.CharField(min_length=2, max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'modifyDataTaskName', 'placeholder': 'Required'}))
    Task_Description = forms.CharField(min_length=2, max_length=512, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'modifyTaskDescription', 'placeholder': 'Required'}))
    Task_Type = forms.ChoiceField(choices=TaskTypes, required=True, widget=forms.Select(attrs={'class': 'form-control', 'id': 'modifyDataTaskType', 'placeholder': 'Required'}))
    Task_StartTime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'modifyTaskStartTime', 'placeholder': 'Start DateTime', 'type': 'datetime-local', 'min': '2020/04/01T000:00', 'max': "2099/12/31T000:00" }))
    Task_EndTime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'modifyTaskEndTime', 'placeholder': 'End DateTime', 'type': 'datetime-local', 'min': '2020/04/01T000:00', 'max': "2099/12/31T000:00" }))

    def clean(self):
        return super(UserTaskUpdateForm, self).clean()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserCredentials
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'dept_residence',
            'username',
            'password',
            'avatar'
            ]

    username = forms.CharField(min_length=2, max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationUsername', 'placeholder': 'Required'}))
    password = forms.CharField(min_length=2, max_length=128, required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'validationPassword', 'placeholder': 'Required'}))
    confirm_password = forms.CharField(min_length=2, max_length=128, required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'validationPassword', 'placeholder': 'Required'}))
    first_name = forms.CharField(min_length=2, max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}))
    middle_name = forms.CharField(min_length=2, max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    last_name = forms.CharField(min_length=2, max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}))
    email = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Required'}))
    avatar = forms.ImageField(required=False, allow_empty_file=True, widget=forms.FileInput(attrs={'accept': 'image/jpg, image/jpeg, image/png', 'class':'form-control-file', 'type':'file'}))
    dept_residence = forms.ModelChoiceField(queryset=UserDepartment.objects.all(), widget=forms.Select(attrs={'class': 'custom-select', 'id':'requireDeptResidence', 'placeholder': 'Required'}), to_field_name='Department_Name', empty_label="Nothing Selected...")

    def clean(self, *args, **kwargs):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        objectDuplicateCheck = UserCredentials.objects.filter(
            username=cleaned_data['username'],
            first_name=cleaned_data['first_name'],
            last_name=cleaned_data['last_name'],
            email=cleaned_data['email']
            ).count()

        if objectDuplicateCheck:
            raise forms.ValidationError("Some of your credentials are conflicting with the existing accounts! Did you register before? Ask the developer please.")

        if password != confirm_password:
            raise forms.ValidationError("Your Password and Password Confirmation Field does not match!")

        return cleaned_data