# Generated by Django 3.1.3 on 2021-11-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20211104_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='borrowed_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
