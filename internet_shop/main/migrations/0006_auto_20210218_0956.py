# Generated by Django 3.1.6 on 2021-02-18 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210218_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slag',
            new_name='slug',
        ),
    ]
