# Generated by Django 4.1.4 on 2023-01-13 06:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
