# Generated by Django 3.2.4 on 2022-02-19 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]