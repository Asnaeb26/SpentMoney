# Generated by Django 3.2.3 on 2021-07-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_spentmoney_time_input'),
    ]

    operations = [
        migrations.CreateModel(
            name='Randomiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
    ]
