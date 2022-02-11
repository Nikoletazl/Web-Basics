from random import choices

from Demos.win32cred_demo import attrs
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.shortcuts import redirect, render

from employee_app.employees.models import Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter First name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             },
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#     )
#
#     age = forms.IntegerField(
#         validators=(
#             validate_positive,
#         )
#     )
#
#     egn = forms.CharField(
#         max_length=15,
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             ('', 'Software Developer'),
#             ('', 'QA Engineer'),
#             ('', 'DevOps Specialist'),
#         )
#     )
#
#     company = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES),
#     )
#

class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model = Employee

        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'},
            )
        }


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }


class CreateEmployeeForm(EmployeeForm):
    pass


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
        )
    )


def home(request):
    return render(request, 'index.html')


def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     egn=employee_form.cleaned_data['egn'],
            #     company=employee_form.cleaned_data['company'],
            #     department_id=1,
            # )
            # emp = Employee(
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            employee_form.save()
            return redirect('index')

    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')
    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'employees/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "POST":
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit.html', context)

