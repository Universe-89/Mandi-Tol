# Generated by Django 4.0.3 on 2022-06-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tol', '0012_auto_20220604_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_register',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='toldiary',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
