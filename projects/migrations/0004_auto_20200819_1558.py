# Generated by Django 3.1 on 2020-08-19 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200819_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='project',
            new_name='projects',
        ),
    ]