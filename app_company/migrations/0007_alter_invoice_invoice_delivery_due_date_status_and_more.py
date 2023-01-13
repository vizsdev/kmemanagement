# Generated by Django 4.1.4 on 2023-01-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0006_alter_employee_employee_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_delivery_due_date_status',
            field=models.CharField(choices=[('', 'Select Status'), ('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_finance_date_status',
            field=models.CharField(choices=[('', 'Select Status'), ('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_mra_date_status',
            field=models.CharField(choices=[('', 'Select Status'), ('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_pac_date_status',
            field=models.CharField(choices=[('', 'Select Status'), ('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=10),
        ),
    ]
