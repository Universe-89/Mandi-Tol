# Generated by Django 3.1 on 2022-06-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0004_entry_date_modified_alter_entry_iscredit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='toldiaryadat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
