import datetime
from datetime import datetime
from django.db import connections

from django.http import HttpResponse
from django.shortcuts import render

# import all the models
from.models import *

# Create your views here.

# db quries tutorial
# https://docs.djangoproject.com/en/3.2/topics/db/queries/#creating-objects

def index(request):
    # return HttpResponse(Employees.objects.all())
    return render(request, 'oracletest/index.html', {
        'employeeList' : Employees.objects.all(),
    })

def employeeById(request, employeeId):
    print(f"employee id: {employeeId}")
    with connections['hr_db'].cursor() as cursor:
        cursor.execute(f"SELECT * from employees WHERE EMPLOYEE_ID = {employeeId}")
        employee_data_as_list = cursor.fetchone()
        job_id = employee_data_as_list[6]
        print(f"job id= {job_id}")
        cursor.execute("SELECT * from JOBS WHERE JOB_ID = %s ", [job_id])
        job = cursor.fetchone()
        print(job)

    
    return render(request, 'oracletest/employee.html', {
        'e' : Employees.toEmployee(employee_data_as_list, Jobs.toJob(job))
    })

from rest_framework.decorators import api_view
from rest_framework.response import *

@api_view(['GET'])
def api_employee(req):
    with connections['hr_db'].cursor() as cursor:
        cursor.execute(f"SELECT * from employees")
        employeeList = dictfetchall(cursor)
    
    return Response(employeeList)

@api_view(['GET'])
def api_employeeById(request, employeeId):
    print(f"employee id: {employeeId}")
    with connections['hr_db'].cursor() as cursor:
        cursor.execute(f"SELECT * from employees WHERE EMPLOYEE_ID = {employeeId}")
        employee_data_as_list = cursor.fetchone()
        job_id = employee_data_as_list[6]
        print(f"job id= {job_id}")
        cursor.execute("SELECT * from JOBS WHERE JOB_ID = %s ", [job_id])
        job = cursor.fetchone()
        print(job)

    return Response( Employees.toEmployee(employee_data_as_list, Jobs.toJob(job)) )
    
@api_view(['GET'])
def api_jobs(req):
    with connections['hr_db'].cursor() as cursor:
        cursor.execute("SELECT * from jobs")
        jobList = dictfetchall(cursor)
    
    return Response(jobList)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]



