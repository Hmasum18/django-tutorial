from django.db import models

# Create your models here.
from django.db import models

class Countries(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(max_length=40, blank=True, null=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    manager = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=25)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'
    
    def toEmployee(data, job=None):
        return {
            'employee_id' : data[0],
            'first_name' : data[1],
            'last_name' : data[2],
            'email' : data[3],
            'phone_number' : data[4],
            'hire_date' : data[5],
            'job' : job,
            'salary' : data[7],
            'commission_pct' : data[8],
            'manager' : data[9],
            'department' : data[10],
        }


class JobHistory(models.Model):
    employee = models.OneToOneField(Employees, models.DO_NOTHING, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_history'
        unique_together = (('employee', 'start_date'),)


class Jobs(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10)
    job_title = models.CharField(max_length=35)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'

    def toJob(data):
        return {
            'job_id': data[0],
            'job_title' : data[1],
            'min_salary' : data[2],
            'max_salary' : data[3]
        }

class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    street_address = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Regions(models.Model):
    region_id = models.FloatField(primary_key=True)
    region_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class Tt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tt'