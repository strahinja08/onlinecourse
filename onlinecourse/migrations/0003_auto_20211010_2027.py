# Generated by Django 3.1.3 on 2021-10-10 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20211010_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_id',
        ),
    ]
