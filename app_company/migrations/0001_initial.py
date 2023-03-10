# Generated by Django 4.1.4 on 2023-01-13 06:24

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_updated_by', models.CharField(auto_created=True, max_length=50)),
                ('company_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company_name', models.TextField(max_length=50)),
                ('company_location', models.CharField(max_length=100)),
                ('company_est', models.CharField(max_length=10)),
                ('company_created_at', models.DateTimeField(auto_now_add=True)),
                ('company_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('employee_firstname', models.CharField(max_length=50)),
                ('employee_middlename', models.CharField(max_length=50)),
                ('employee_lastname', models.CharField(max_length=50)),
                ('employee_birth', models.CharField(max_length=20)),
                ('employee_gender', models.CharField(choices=[('', 'Select Gender'), ('M', 'MALE'), ('F', 'FEMALE')], default='', max_length=2)),
                ('employee_nationality', django_countries.fields.CountryField(max_length=2)),
                ('employee_passport', models.CharField(max_length=30, unique=True)),
                ('employee_passport_exp', models.DateTimeField(max_length=20)),
                ('employee_eid', models.CharField(max_length=30, unique=True)),
                ('employee_eid_exp', models.DateTimeField()),
                ('employee_visa', models.CharField(max_length=30, unique=True)),
                ('employee_visa_exp', models.DateTimeField(max_length=20)),
                ('employee_created_at', models.DateTimeField(auto_now_add=True)),
                ('employee_updated_at', models.DateTimeField(auto_now=True)),
                ('employee_photo', models.FileField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('invoice_customer_po', models.CharField(max_length=15)),
                ('invoice_order_quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('invoice_foc_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('invoice_foc_quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('invoice_unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice_net_value', models.DecimalField(decimal_places=0, max_digits=10)),
                ('invoice_delivery_due_date', models.DateTimeField(max_length=10)),
                ('invoice_issue_date', models.DateTimeField(max_length=10)),
                ('invoice_number', models.CharField(max_length=20)),
                ('invoice_mra_date', models.DateTimeField(max_length=10)),
                ('invoice_pac_date', models.DateTimeField(max_length=10)),
                ('invoice_finance_date', models.DateTimeField(max_length=10)),
                ('invoice_created_at', models.DateTimeField(auto_now_add=True)),
                ('invoice_updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_document_0', models.FileField(blank=True, null=True, upload_to='documents')),
                ('invoice_document_1', models.FileField(blank=True, null=True, upload_to='documents')),
                ('invoice_document_2', models.FileField(blank=True, null=True, upload_to='documents')),
                ('invoice_document_3', models.FileField(blank=True, null=True, upload_to='documents')),
                ('invoice_document_4', models.FileField(blank=True, null=True, upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('role_name', models.CharField(max_length=20, unique=True)),
                ('role_created_at', models.DateTimeField(auto_now_add=True)),
                ('role_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TDesignation',
            fields=[
                ('designation_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('designation_start', models.CharField(max_length=20, null=True)),
                ('designation_end', models.CharField(max_length=20, null=True)),
                ('designation_created_at', models.DateTimeField(auto_now_add=True)),
                ('designation_updated_at', models.DateTimeField(auto_now=True)),
                ('designation_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_company.employee', unique=True)),
                ('designation_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_company.role')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('department_name', models.CharField(max_length=50)),
                ('department_created_at', models.DateTimeField(auto_now_add=True)),
                ('department_updated_at', models.DateTimeField(auto_now=True)),
                ('department_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_company.company')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('attendance_in', models.CharField(blank=True, max_length=20, null=True)),
                ('attendance_timein', models.DateTimeField(auto_now_add=True)),
                ('attendance_out', models.CharField(blank=True, max_length=20, null=True)),
                ('attendance_timeout', models.DateTimeField(auto_now=True, null=True)),
                ('attendance_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_company.employee')),
            ],
        ),
    ]
