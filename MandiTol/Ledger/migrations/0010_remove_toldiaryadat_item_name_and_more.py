# Generated by Django 4.0.3 on 2022-08-25 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0009_entry_billid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toldiaryadat',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='toldiaryadat',
            name='party_name',
        ),
        migrations.DeleteModel(
            name='BillMetaData',
        ),
        migrations.DeleteModel(
            name='TolDiaryAdat',
        ),
    ]
