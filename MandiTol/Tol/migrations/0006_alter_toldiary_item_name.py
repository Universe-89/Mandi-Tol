# Generated by Django 4.0.3 on 2022-04-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tol', '0005_alter_toldiary_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toldiary',
            name='item_name',
            field=models.CharField(max_length=20),
        ),
    ]