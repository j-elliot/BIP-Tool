# Generated by Django 3.2.3 on 2021-06-03 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bipApp', '0008_auto_20210603_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='owner_id',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='contractor',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='contractor',
            old_name='entity_id',
            new_name='entity',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='entity_id',
            new_name='entity',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='status_id',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='dependency',
            old_name='predecessor_id',
            new_name='predecessor',
        ),
        migrations.RenameField(
            model_name='dependency',
            old_name='successor_id',
            new_name='successor',
        ),
        migrations.RenameField(
            model_name='dependency',
            old_name='type_id',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='entity_id',
            new_name='entity',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_status_id',
            new_name='invoice_status',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='report_id',
            new_name='report',
        ),
        migrations.RenameField(
            model_name='invoice_line_item',
            old_name='invoice_id',
            new_name='invoice',
        ),
        migrations.RenameField(
            model_name='invoice_line_item',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='invoice_transaction',
            old_name='invoice_id',
            new_name='invoice',
        ),
        migrations.RenameField(
            model_name='invoice_transaction',
            old_name='transaction_id',
            new_name='transaction',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='vendor_id',
            new_name='vendor',
        ),
        migrations.RenameField(
            model_name='item_category',
            old_name='parent_category_id',
            new_name='parent_category',
        ),
        migrations.RenameField(
            model_name='item_note',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='item_supporting_doc',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='entity_id',
            new_name='entity',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='owner_id',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='project_note',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_supporting_doc',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='receipt_status_id',
            new_name='receipt_status',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='report_id',
            new_name='report',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='vendor_id',
            new_name='vendor',
        ),
        migrations.RenameField(
            model_name='receipt_line_item',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='receipt_line_item',
            old_name='receipt_id',
            new_name='receipt',
        ),
        migrations.RenameField(
            model_name='receipt_transaction',
            old_name='receipt_id',
            new_name='receipt',
        ),
        migrations.RenameField(
            model_name='receipt_transaction',
            old_name='transaction_id',
            new_name='transaction',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='report_note',
            old_name='report_id',
            new_name='report',
        ),
        migrations.RenameField(
            model_name='report_supporting_doc',
            old_name='report_id',
            new_name='report',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='assignee_id',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='task_note',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='task_supporting_doc',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='time_clock_entry',
            old_name='ledger_entry_id',
            new_name='ledger_entry',
        ),
        migrations.RenameField(
            model_name='time_clock_entry',
            old_name='report_id',
            new_name='report',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_id',
            new_name='transaction',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='entity_id',
            new_name='entity',
        ),
    ]