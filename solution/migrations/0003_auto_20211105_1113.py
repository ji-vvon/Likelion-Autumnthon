# Generated by Django 3.2.9 on 2021-11-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_auto_20211104_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
