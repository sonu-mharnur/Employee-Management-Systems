
from django.urls import path
from .views import *

urlpatterns = [
    path('departments/', DepartmentListCreate.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroy.as_view(), name='department-detail'),
    path('employees/', EmployeeListCreate.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail'),
    path('employees-with-department/', EmployeeWithDepartmentList.as_view(), name='employee-with-department-list'),
]
