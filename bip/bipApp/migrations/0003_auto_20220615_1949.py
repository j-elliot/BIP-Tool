# Generated by Django 3.2.3 on 2022-06-15 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0002_auto_20220218_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='closing',
        ),
        migrations.RemoveField(
            model_name='report',
            name='opening',
        ),
        migrations.RemoveField(
            model_name='task',
            name='closing',
        ),
        migrations.RemoveField(
            model_name='task',
            name='opening',
        ),
    ]