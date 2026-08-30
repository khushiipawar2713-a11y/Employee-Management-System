from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max, Min
from django.core.paginator import Paginator
from django.http import HttpResponse

import openpyxl

from .models import Employee
from .forms import EmployeeForm

from django.db.models import Count
from django.db.models import Max, Min, Count

from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Employee List
@login_required
def employee_list(request):
    query = request.GET.get("q")

    if query:
        employees = Employee.objects.filter(
            name__icontains=query
        ).order_by("id")
    else:
        employees = Employee.objects.all().order_by("id")

    paginator = Paginator(employees, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "employees/employee_list.html", {
        "employees": page_obj,
        "page_obj": page_obj,
    })


# Add Employee
@login_required
def add_employee(request):
    if request.method == "POST":
        print(request.FILES) 
        form = EmployeeForm(
    request.POST,
    request.FILES
)

        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect("employee_list")

    else:
        form = EmployeeForm()

    return render(request, "employees/add_employee.html", {
        "form": form
    })


# Update Employee
@login_required
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect("employee_list")

    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employees/update_employee.html", {
        "form": form
    })


# View Employee
@login_required
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    return render(request, "employees/employee_detail.html", {
        "employee": employee
    })


# Delete Employee
@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()

    messages.success(request, "Employee deleted successfully!")

    return redirect("employee_list")


# Dashboard

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()
    total_departments = Employee.objects.values("department").distinct().count()

    highest_salary = Employee.objects.aggregate(Max("salary"))
    lowest_salary = Employee.objects.aggregate(Min("salary"))

    department_data = Employee.objects.values("department").annotate(total=Count("id"))

    context = {
        "total_employees": total_employees,
        "total_departments": total_departments,
        "highest_salary": highest_salary["salary__max"],
        "lowest_salary": lowest_salary["salary__min"],
        "department_data": department_data,
    }

    return render(request, "employees/dashboard.html", context)

# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("employee_list")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "employees/login.html")


# Logout
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")


# Export Excel
@login_required
def export_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Employees"

    ws.append([
        "Name",
        "Email",
        "Phone",
        "Department",
        "Designation",
        "Salary",
        "Joining Date",
    ])

    employees = Employee.objects.all().order_by("id")

    for emp in employees:
        ws.append([
            emp.name,
            emp.email,
            emp.phone,
            emp.department,
            emp.designation,
            emp.salary,
            str(emp.joining_date),
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="employees.xlsx"'

    wb.save(response)

    return response

def employee_pdf(request):

    employees = Employee.objects.all()

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="employee_report.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setTitle("Employee Report")

    y = 800

    pdf.drawString(
        200,
        y,
        "Employee Management Report"
    )

    y -= 50


    for employee in employees:

        data = (
            f"Name: {employee.name} | "
            f"Email: {employee.email} | "
            f"Department: {employee.department} | "
            f"Salary: {employee.salary}"
        )

        pdf.drawString(
            50,
            y,
            data
        )

        y -= 30


        if y < 50:
            pdf.showPage()
            y = 800


    pdf.save()

    return response