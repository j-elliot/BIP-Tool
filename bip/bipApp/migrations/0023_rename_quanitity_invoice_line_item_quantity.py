# Generated by Django 3.2.3 on 2021-06-12 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0022_invoice_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice_line_item',
            old_name='quanitity',
            new_name='quantity',
        ),
    ]
