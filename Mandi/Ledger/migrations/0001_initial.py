# Generated by Django 4.1 on 2022-08-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('opBal', models.IntegerField()),
                ('GSTIN', models.CharField(max_length=15)),
                ('phoneNumber', models.CharField(max_length=10)),
            ],
        ),
    ]
