# Generated by Django 3.2.4 on 2022-01-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0029_alter_report_sub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='birthdate',
            new_name='birthdate_dep',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='children',
            new_name='children_dep',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='interests',
            new_name='interests_dep',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='spouse',
            new_name='spouse_dep',
        ),
        migrations.AddField(
            model_name='customer',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='birthdate'),
        ),
        migrations.AddField(
            model_name='customer',
            name='interest',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='path',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='spouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spouse', to='bipApp.entity'),
        ),
        migrations.AddField(
            model_name='project',
            name='path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
