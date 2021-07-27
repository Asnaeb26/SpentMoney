# Generated by Django 3.2.3 on 2021-07-28 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Homepage', '0024_auto_20210725_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='spentmoney',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
