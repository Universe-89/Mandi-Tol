# Generated by Django 3.1 on 2022-08-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tol', '0013_alter_stock_register_id_alter_toldiary_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_register',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='toldiary',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]