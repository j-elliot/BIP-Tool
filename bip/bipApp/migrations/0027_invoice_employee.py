# Generated by Django 3.2.3 on 2021-06-20 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0026_alter_invoice_submitted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='employee',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.CASCADE, to='bipApp.entity'),
            preserve_default=False,
        ),
    ]
