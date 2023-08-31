# from django.db import models
from django.db import models
# Create your models here.


class Departments(models.Model):
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50, null=True, blank=True)

class Position(models.Model):
    title = models.CharField(max_length=50)

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    sur_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    positions = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    reporting_time = models.TimeField()
    leaving_time = models.TimeField()
    front_image = models.ImageField(upload_to='employee_images/')
    right_image = models.ImageField(upload_to='employee_images/')
    left_image = models.ImageField(upload_to='employee_images/')
    fingerprint = models.BinaryField()


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    date = models.DateField()
    overtime_increment = models.DecimalField(max_digits=5, decimal_places=2)
    late_decrement = models.DecimalField(max_digits=5, decimal_places=2)

class DeductionReason(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason_description = models.CharField(max_length=100)
    


class SalaryDeduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE)
    deduction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.ForeignKey(DeductionReason, on_delete=models.CASCADE)
    confirmed = models.BooleanField()
    deduction_timestamp = models.DateTimeField()

class AdminUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password_hash = models.CharField(max_length=128)
    

class DeductionConfirmation(models.Model):
    deduction = models.ForeignKey(SalaryDeduction, on_delete=models.CASCADE)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    confirmation_timestamp = models.DateTimeField()

class Overtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    requested_date = models.DateField()
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    overtime_minutes = models.DecimalField(max_digits=8, decimal_places=2)
    overtime_reason = models.ForeignKey(DeductionReason, on_delete=models.CASCADE)
    confirmed = models.BooleanField()

class OvertimeConfirmation(models.Model):
    overtime_request = models.ForeignKey(Overtime, on_delete=models.CASCADE)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    confirmation_timestamp = models.DateTimeField()
