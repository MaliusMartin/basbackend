from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from  ImperialEmployeesApp.models import Employee, AttendanceRecord,DeductionConfirmation,SalaryDeduction,AdminUser,DeductionReason,Overtime,OvertimeConfirmation,Departments,Positions 
from ImperialEmployeesApp.serializers import EmployeeSerializer,AdminUserSerializer,AttendanceRecordSerializer,DeductionConfirmationSerializer,SalaryDeductionSerializer,AdminUserSerializer,DeductionReasonSerializer,OvertimeSerializer,OvertimeConfirmationSerializer,DepartmentsSerializer,PositionsSerializer



@csrf_exempt
def employee_api(request, id=0):
    if request.method == "GET":
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete Successful", safe=False)

 
    
@csrf_exempt
def salary_deduction_api(request, id=0):
    if request.method == "GET":
        deductions = SalaryDeduction.objects.all()
        deductions_serializer = SalaryDeductionSerializer(deductions, many=True)
        return JsonResponse(deductions_serializer.data, safe=False)
    elif request.method == "POST":
        deduction_data = JSONParser().parse(request)
        deductions_serializer = SalaryDeductionSerializer(data=deduction_data)
        if deductions_serializer.is_valid():
            deductions_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        deduction_data = JSONParser().parse(request)
        deduction = SalaryDeduction.objects.get(DeductionID=deduction_data['DeductionID'])
        deductions_serializer = SalaryDeductionSerializer(deduction, data=deduction_data)
        if deductions_serializer.is_valid():
            deductions_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        deduction = SalaryDeduction.objects.get(DeductionID=id)
        deduction.delete()
        return JsonResponse("Delete Successful", safe=False)
    
    
@csrf_exempt
def attendance_records_api(request, id=0):
    if request.method == "GET":
        records = AttendanceRecord.objects.all()
        records_serializer = AttendanceRecordSerializer(records, many=True)
        return JsonResponse(records_serializer.data, safe=False)
    elif request.method == "POST":
        record_data = JSONParser().parse(request)
        records_serializer = AttendanceRecordSerializer(data=record_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        record_data = JSONParser().parse(request)
        record = AttendanceRecord.objects.get(RecordID=record_data['RecordID'])
        records_serializer = AttendanceRecordSerializer(record, data=record_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        record = AttendanceRecord.objects.get(RecordID=id)
        record.delete()
        return JsonResponse("Delete Successful", safe=False)

@csrf_exempt
def deduction_confirmation_api(request, id=0):
    if request.method == "GET":
        deductions = DeductionConfirmation.objects.all()
        deductions_serializer = DeductionConfirmationSerializer(deductions, many=True)
        return JsonResponse(deductions_serializer.data, safe=False)
    elif request.method == "POST":
        deduction_data = JSONParser().parse(request)
        deductions_serializer = DeductionConfirmationSerializer(data=deduction_data)
        if deductions_serializer.is_valid():
            deductions_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        deduction_data = JSONParser().parse(request)
        deduction = DeductionConfirmation.objects.get(ConfirmationID=deduction_data['ConfirmationID'])
        deductions_serializer = DeductionConfirmationSerializer(deduction, data=deduction_data)
        if deductions_serializer.is_valid():
            deductions_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        deduction = DeductionConfirmation.objects.get(ConfirmationID=id)
        deduction.delete()
        return JsonResponse("Delete Successful", safe=False)
    
    
@csrf_exempt
def admin_user_api(request, id=0):
    if request.method == "GET":
        admin_users = AdminUser.objects.all()
        admin_users_serializer = AdminUserSerializer(admin_users, many=True)
        return JsonResponse(admin_users_serializer.data, safe=False)
    elif request.method == "POST":
        admin_user_data = JSONParser().parse(request)
        admin_users_serializer = AdminUserSerializer(data=admin_user_data)
        if admin_users_serializer.is_valid():
            admin_users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        admin_user_data = JSONParser().parse(request)
        admin_user = AdminUser.objects.get(AdminUserID=admin_user_data['AdminUserID'])
        admin_users_serializer = AdminUserSerializer(admin_user, data=admin_user_data)
        if admin_users_serializer.is_valid():
            admin_users_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        admin_user = AdminUser.objects.get(AdminUserID=id)
        admin_user.delete()
        return JsonResponse("Delete Successful", safe=False)


@csrf_exempt
def deduction_reason_api(request, id=0):
    if request.method == "GET":
        deduction_reasons = DeductionReason.objects.all()
        deduction_reasons_serializer = DeductionReasonSerializer(deduction_reasons, many=True)
        return JsonResponse(deduction_reasons_serializer.data, safe=False)
    elif request.method == "POST":
        deduction_reason_data = JSONParser().parse(request)
        deduction_reasons_serializer = DeductionReasonSerializer(data=deduction_reason_data)
        if deduction_reasons_serializer.is_valid():
            deduction_reasons_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        deduction_reason_data = JSONParser().parse(request)
        deduction_reason = DeductionReason.objects.get(ReasonID=deduction_reason_data['ReasonID'])
        deduction_reasons_serializer = DeductionReasonSerializer(deduction_reason, data=deduction_reason_data)
        if deduction_reasons_serializer.is_valid():
            deduction_reasons_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        deduction_reason = DeductionReason.objects.get(ReasonID=id)
        deduction_reason.delete()
        return JsonResponse("Delete Successful", safe=False)
    
    
@csrf_exempt
def overtime_api(request, id=0):
    if request.method == "GET":
        overtimes = Overtime.objects.all()
        overtimes_serializer = OvertimeSerializer(overtimes, many=True)
        return JsonResponse(overtimes_serializer.data, safe=False)
    elif request.method == "POST":
        overtime_data = JSONParser().parse(request)
        overtimes_serializer = OvertimeSerializer(data=overtime_data)
        if overtimes_serializer.is_valid():
            overtimes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        overtime_data = JSONParser().parse(request)
        overtime = Overtime.objects.get(RequestID=overtime_data['RequestID'])
        overtimes_serializer = OvertimeSerializer(overtime, data=overtime_data)
        if overtimes_serializer.is_valid():
            overtimes_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        overtime = Overtime.objects.get(RequestID=id)
        overtime.delete()
        return JsonResponse("Delete Successful", safe=False)
    
@csrf_exempt
def overtime_confirmation_api(request, id=0):
    if request.method == "GET":
        confirmations = OvertimeConfirmation.objects.all()
        confirmations_serializer = OvertimeConfirmationSerializer(confirmations, many=True)
        return JsonResponse(confirmations_serializer.data, safe=False)
    elif request.method == "POST":
        confirmation_data = JSONParser().parse(request)
        confirmations_serializer = OvertimeConfirmationSerializer(data=confirmation_data)
        if confirmations_serializer.is_valid():
            confirmations_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        confirmation_data = JSONParser().parse(request)
        confirmation = OvertimeConfirmation.objects.get(ConfirmationID=confirmation_data['ConfirmationID'])
        confirmations_serializer = OvertimeConfirmationSerializer(confirmation, data=confirmation_data)
        if confirmations_serializer.is_valid():
            confirmations_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        confirmation = OvertimeConfirmation.objects.get(ConfirmationID=id)
        confirmation.delete()
        return JsonResponse("Delete Successful", safe=False)
    
    
@csrf_exempt
def departments_api(request, id=0):
    if request.method == "GET":
        departments = Departments.objects.all()
        departments_serializer = DepartmentsSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(id=department_data['id'])
        departments_serializer = DepartmentsSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        department = Departments.objects.get(id=id)
        department.delete()
        return JsonResponse("Delete Successful", safe=False)


@csrf_exempt
def positions_api(request, id=0):
    if request.method == "GET":
        position = Positions.objects.all()
        positions_serializer = PositionsSerializer(position, many=True)
        return JsonResponse(positions_serializer.data, safe=False)
    elif request.method == "POST":
        position_data = JSONParser().parse(request)
        positions_serializer = PositionsSerializer(data=position_data)
        if positions_serializer.is_valid():
            positions_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == "PUT":
        position_data = JSONParser().parse(request)
        position = Positions.objects.get(id=position_data['id'])
        positions_serializer = PositionsSerializer(position, data=position_data)
        if positions_serializer.is_valid():
            positions_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        position = Positions.objects.get(id=id)
        position.delete()
        return JsonResponse("Delete Successful", safe=False)