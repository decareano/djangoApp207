# Generated by Django 2.0.7 on 2020-05-06 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0002_auto_20200506_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='ICU_currently',
            new_name='icu_currently',
        ),
    ]
