# Generated by Django 3.2.3 on 2021-06-12 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0020_alter_item_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt_line_item',
            old_name='quanitity',
            new_name='quantity',
        ),
    ]