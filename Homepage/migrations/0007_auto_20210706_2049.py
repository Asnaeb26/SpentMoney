# Generated by Django 3.2.3 on 2021-07-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0006_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='person3',
            name='avatar',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person3',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
