# Generated by Django 4.1.4 on 2023-01-13 09:57

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0007_alter_invoice_invoice_delivery_due_date_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_est',
            field=models.DateTimeField(max_length=10),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_location',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]