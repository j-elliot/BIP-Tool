# Generated by Django 3.2.3 on 2021-06-11 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0017_auto_20210606_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bipApp.account'),
        ),
        migrations.AlterField(
            model_name='item',
            name='reference',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item_category',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bipApp.item_category'),
        ),
    ]
