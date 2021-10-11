# Generated by Django 3.2.3 on 2021-06-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0023_rename_quanitity_invoice_line_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='closing',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='opening',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='closing',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='opening',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='time_clock_entry',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='time_clock_entry',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date'),
        ),
    ]
