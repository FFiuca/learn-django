# Generated by Django 4.1.7 on 2023-05-17 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category_id',
            new_name='category',
        ),
    ]
