# Generated by Django 3.2.3 on 2021-06-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0019_auto_20210611_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]