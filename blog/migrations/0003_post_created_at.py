# Generated by Django 4.1.7 on 2023-03-05 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_email_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
