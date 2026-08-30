from django.urls import path
from .views import employee_pdf
from .views import (
    employee_list,
    add_employee,
    update_employee,
    delete_employee,
    dashboard,
    login_user,
    logout_user,
    employee_detail,
    export_excel,
)

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("add/", add_employee, name="add_employee"),

    path("view/<int:id>/", employee_detail, name="employee_detail"),
    path("update/<int:id>/", update_employee, name="update_employee"),
    path("delete/<int:id>/", delete_employee, name="delete_employee"),

    path("dashboard/", dashboard, name="dashboard"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("export/", export_excel, name="export_excel"),
    path(
    'employee-pdf/',
    employee_pdf,
    name='employee_pdf'
),
]
