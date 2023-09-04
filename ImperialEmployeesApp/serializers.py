from rest_framework import serializers
from ImperialEmployeesApp.models import Employee, AttendanceRecord, DeductionReason,SalaryDeduction,DeductionConfirmation,Overtime,OvertimeConfirmation, AdminUser,Departments, Positions

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name','middle_name','sur_name','mobile_number','email','department','position','salary',
                  'reporting_time','leaving_time','front_image','right_image','left_image','fingerprint')


class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ('employee','check_in_time','check_out_time','date','overtime_increment',)

class DeductionReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeductionReason
        fields = ('employee','reason_description')
        
class SalaryDeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryDeduction
        fields = ('employee','attendance_record','deduction_amount','reason','confirmed','deduction_timestamp')

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = (' username','email','password_hash')
        
class DeductionConfirmationSerializer(serializers.ModelSerializer):   
    class Meta:
        model = DeductionConfirmation
        fields = ('deduction','admin_user','confirmation_timestamp')
        
class OvertimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overtime
        fields = ('employee','reqested_date','overtime_hours', 'overtime_minutes', 'overtime_reasons', 'confirmed')    
  
        
class OvertimeConfirmationSerializer(serializers.ModelSerializer):
     class Meta:
         model = OvertimeConfirmation
         fields = ('overtime_request','admin_user','confirmation_timestamp')

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department',)

        

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ('position',)
        
            