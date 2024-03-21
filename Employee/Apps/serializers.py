
from rest_framework import serializers
from .models import Employee, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'department_name']

    def get_department_name(self, obj):
        return obj.department.name
