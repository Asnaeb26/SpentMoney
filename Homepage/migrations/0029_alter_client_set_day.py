# Generated by Django 3.2.3 on 2021-08-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0028_client_set_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='set_day',
            field=models.IntegerField(default=1),
        ),
    ]
