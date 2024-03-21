
from rest_framework import generics
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django.db import models

class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeWithDepartmentList(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        department_name = self.request.query_params.get('department_name', None)
        employee_name = self.request.query_params.get('employee_name', None)
        if department_name:
            queryset = queryset.filter(department__name=department_name)
        if employee_name:
            queryset = queryset.filter(name__icontains=employee_name)
        return queryset
