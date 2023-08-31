from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_api),  # Employees API
    path('employee/<int:id>/', views.employee_api),  # Retrieve/Update/Delete specific employee

    path('attendance/', views.attendance_records_api),  # Attendance Records API
    path('attendance/<int:id>/', views.attendance_records_api),  # Retrieve/Update/Delete specific attendance record

    path('deduction-confirmation/', views.deduction_confirmation_api),  # Deduction Confirmation API
    path('deduction-confirmation/<int:id>/', views.deduction_confirmation_api),  # Retrieve/Update/Delete specific deduction confirmation

    path('salary-deduction/', views.salary_deduction_api),  # Salary Deduction API
    path('salary-deduction/<int:id>/', views.salary_deduction_api),  # Retrieve/Update/Delete specific salary deduction

    path('admin-user/', views.admin_user_api),  # Admin User API
    path('admin-user/<int:id>/', views.admin_user_api),  # Retrieve/Update/Delete specific admin user

    path('deduction-reason/', views.deduction_reason_api),  # Deduction Reason API
    path('deduction-reason/<int:id>/', views.deduction_reason_api),  # Retrieve/Update/Delete specific deduction reason

    path('overtime/', views.overtime_api),  # Overtime API
    path('overtime/<int:id>/', views.overtime_api),  # Retrieve/Update/Delete specific overtime

    path('overtime-confirmation/', views.overtime_confirmation_api),  # Overtime Confirmation API
    path('overtime-confirmation/<int:id>/', views.overtime_confirmation_api),  # Retrieve/Update/Delete specific overtime confirmation
    
    path('departments/', views.departments_api),  # Overtime Confirmation API
    path('departments/<int:id>/', views.departments_api),  # Retrieve/Update/Delete specific overtime confirmation
    
]
